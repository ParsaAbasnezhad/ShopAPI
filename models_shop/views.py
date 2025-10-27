from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from .permission import BlocklistPermission
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, IsAdminUser


class ProductView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        permission_classes = [BlocklistPermission]
        serializer = ProductSerializer(data=request.data)
        self.check_object_permissions(request, serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductUpdate(APIView):
    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        permission_classes = [BlocklistPermission]
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        self.check_object_permissions(request, serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        permission_classes = [BlocklistPermission]
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        self.check_object_permissions(request, serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        permission_classes = [IsAdminUser]
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CheckToken(APIView):
    # authentication_classes = [TokenAuthentication]

    def get(self, request):
        return Response(status=status.HTTP_200_OK)
