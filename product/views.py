from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from product.permissions import IsStaffOrReadOnly
from product.models import Category, Product
from product.serializers import CategorySerializer, ProductSerializer

# Create your views here.
# TODO Create Category views. List will be seperate
# Retrieve will also be different. Update Create and Delete will be restricted by
# Same goes for Product


class CategoryListView(ListCreateAPIView):
    permission_classes = [IsStaffOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsStaffOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"


class ProductListView(ListCreateAPIView):
    permission_classes = [IsStaffOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsStaffOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
