from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['created_at', 'is_active']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['updated_at', 'created_at', 'id']
        read_only_fields = ['stock', 'image']

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("نام باید حداقل ۲ کاراکتر باشد.")
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("قیمت نمی‌تواند منفی باشد.")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("موجودی نمی‌تواند منفی باشد.")
        return value
