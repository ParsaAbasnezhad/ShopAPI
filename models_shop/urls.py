from django.urls import path
from .views import ProductView, ProductUpdate, CheckToken
from rest_framework.authtoken import views

urlpatterns = [
    # برای get و post
    path('products/', ProductView.as_view(), name='product-list'),
    # برای getکردن یهک product و put و patch و delete
    path('products/<int:pk>/', ProductUpdate.as_view(), name='product-detail'),
    path('check/', CheckToken.as_view(), name='check-token'),
    #     آدرس گرفتن token
    path('login/', views.obtain_auth_token, name='get-token'),
]

# ProductUpdate
# ProductView
