from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductsViewModel

router = DefaultRouter()
router.register(r'products', ProductsViewModel, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
