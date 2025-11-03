from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError, PermissionDenied
from .models import User
from .serializers import UserSerializer


class UserView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def handle_exception(self, exc):
        if isinstance(exc, (ValidationError, PermissionDenied)):
            return Response({'error': str(exc)}, status=status.HTTP_400_BAD_REQUEST)
        elif isinstance(exc, Http404):
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        return super().handle_exception(exc)

    def get(self, request):
        user = request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user

        if 'is_staff' in request.data and not user.is_staff:
            raise PermissionDenied('You do not have permission to change staff status')

        serializer = self.serializer_class(
            instance=user,
            data=request.data,
            partial=True,  # ✅ برای آپدیت جزئی
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
