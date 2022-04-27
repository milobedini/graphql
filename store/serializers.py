from rest_framework import serializers

from .models import Category, Product, ProductImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("id", "image", "alt_text")


class ProductSerializer(serializers.ModelSerializer):
    product_image = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "slug")
