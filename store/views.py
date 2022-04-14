from django.shortcuts import render
from rest_framework import generics

from . import models
from .serializers import ProductSerializer

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
