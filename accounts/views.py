from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError, PermissionDenied
from .models import User
from .permissions import IsUser
from .serializers import UserSerializer


class UserView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def handle_exception(self, exc):
        if isinstance(exc, (ValidationError, PermissionDenied)):
            return Response(
                {'error': str(exc)},
                status=status.HTTP_400_BAD_REQUEST
            )
        elif isinstance(exc, Http404):
            return Response(
                {'error': 'User not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        return super().handle_exception(exc)

    def get(self, request):
        try:
            user = request.user
            if not user.is_authenticated:
                raise PermissionDenied('Authentication required')
                
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': 'Failed to retrieve user data'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request):
        try:
            user = request.user
            if not user.is_authenticated:
                raise PermissionDenied('Authentication required')
                
            # Prevent users from changing sensitive fields
            if 'is_staff' in request.data and not user.is_staff:
                raise PermissionDenied('You do not have permission to change staff status')
                
            serializer = UserSerializer(
                instance=user, 
                data=request.data,
                partial=False,
                context={'request': request}
            )
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
                
            return Response(
                {'error': 'Invalid data', 'details': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
                )
                
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=getattr(e, 'status_code', status.HTTP_500_INTERNAL_SERVER_ERROR)
            )
