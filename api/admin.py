from django.contrib import admin

# Register your models here.

from .models import Product, Shelf, Storage, ProductSize, ProductLocation


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'article', 'price', 'created')


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')


@admin.register(Shelf)
class ShelfAdmin(admin.ModelAdmin):
    list_display = ('id', 'storage', 'number')


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'size')


@admin.register(ProductLocation)
class ProductLocationAdmin(admin.ModelAdmin):
    list_display = ('product_size', 'shelf')
