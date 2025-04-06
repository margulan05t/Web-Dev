from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)  
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'count', 'is_active', 'category', 'category_name') 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class CategoryWithProductsSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)  

    class Meta:
        model = Category
        fields = ('id', 'name', 'products')