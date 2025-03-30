from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)  # Добавляем имя категории
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'count', 'is_active', 'category', 'category_name') # include category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class CategoryWithProductsSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)  # Включаем сериализованные продукты

    class Meta:
        model = Category
        fields = ('id', 'name', 'products')