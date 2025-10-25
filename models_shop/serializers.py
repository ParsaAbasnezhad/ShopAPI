from .models import Category, Product
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        exclude = ['created_at','is_active']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['updated_at', 'created_at','stock','id']
        read_only_fields = ['name', 'description','stock','image']

        def vlidate_name(self, value):
            if value.lenght() < 2:
                raise serializers.ValidationError("Name must be at least 2 characters long")
            return value

        def validate_price(self, value):
            if value < 0:
                raise serializers.ValidationError("Price cannot be negative")
            return value

        def validate_stock(self, value):
            if value < 0:
                raise serializers.ValidationError("Stock cannot be negative")
            return value
