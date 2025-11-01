from django.urls import path
from .views import ProductView, ProductUpdate, CheckToken

urlpatterns = [
    # برای get و post
    path('products/', ProductView.as_view(), name='product-list'),
    # برای getکردن یهک product و put و patch و delete
    path('products/<int:pk>/', ProductUpdate.as_view(), name='product-detail'),
    path('check/', CheckToken.as_view(), name='check-token'),

]

# ProductUpdate
# ProductView
