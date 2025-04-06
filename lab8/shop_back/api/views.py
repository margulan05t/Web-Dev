from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer, CategoryWithProductsSerializer
from django.shortcuts import get_object_or_404

class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get(self, request, id):
        category = get_object_or_404(Category, id=id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class CategoryProducts(APIView):
    def get(self, request, id):
       category = get_object_or_404(Category, id=id)
       serializer = CategoryWithProductsSerializer(category)
       return Response(serializer.data)
    
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # Указываем, что для поиска используется поле 'pk'

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # Указываем, что для поиска используется поле 'pk'

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk' # Указываем, что для поиска используется поле 'pk'

class CategoryProducts(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['pk']
        return Product.objects.filter(category_id=category_id)