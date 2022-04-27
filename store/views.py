from django.shortcuts import render
from rest_framework import generics

from . import models
from .serializers import CategorySerializer, ProductSerializer

# Create your views here.


class ProductListView(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = ProductSerializer


class Product(generics.RetrieveAPIView):
    # will match the slug field to the db. Allows more readable urls.
    lookup_field = "slug"
    queryset = models.Product.objects.all()
    serializer_class = ProductSerializer


class CategoryItemView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return models.Product.objects.filter(category__slug=self.kwargs["slug"])


class CategoryListView(generics.ListAPIView):
    # level one only shows categories that are one below the top level (e.g. shoes are in men - level 0), so won't show boots
    # which are level 2.
    queryset = models.Category.objects.filter(level=1)
    serializer_class = CategorySerializer
