from api.models import Product, Storage, Shelf, ProductSize, ProductLocation
from api.serializers import ProductSerializer, StorageSerializer, \
    ShelfSerializer, ProductSizeSerializer, \
    ProductLocationSerializer
from rest_framework import generics


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StorageList(generics.ListCreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


class StorageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


class ShelfList(generics.ListCreateAPIView):
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer


class ShelfDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer


class ProductSizeList(generics.ListCreateAPIView):
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeSerializer


class ProductSizeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeSerializer


class ProductLocationList(generics.ListCreateAPIView):
    queryset = ProductLocation.objects.all()
    serializer_class = ProductLocationSerializer


class ProductLocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductLocation.objects.all()
    serializer_class = ProductLocationSerializer
