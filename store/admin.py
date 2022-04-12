from ast import Store

from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    Category,
    Product,
    ProductImage,
    ProductSpecification,
    ProductSpecificationValue,
    ProductType,
)

# Register your models here.

admin.site.register(Category, MPTTModelAdmin)

# This allows 2 tables to be edited inline (helpful when very interlinked)
class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification


# Get Product Type and Product Specs next to each other in admin.
@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationInline,
    ]


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductSpecificationvalueInline(admin.TabularInline):
    model = ProductSpecificationValue


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
        ProductSpecificationvalueInline,
    ]
