from rest_framework import generics
from rest_framework.exceptions import NotFound
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  # Используем pk для поиска

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'  # Используем pk для поиска

class CategoryProducts(generics.ListAPIView):
    serializer_class = ProductSerializer # Используем ProductSerializer для списка продуктов

    def get_queryset(self):
        category_id = self.kwargs.get('pk') # Получаем pk из URL
        if category_id is not None:
            return Product.objects.filter(category_id=category_id)
        else:
            raise NotFound("Category ID was not provided")