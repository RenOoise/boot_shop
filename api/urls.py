from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>', views.ProductDetail.as_view()),
    path('storages/', views.StorageList.as_view()),
    path('storages/<int:pk>', views.StorageDetail.as_view()),
    path('shelves/', views.ShelfList.as_view()),
    path('shelves/<int:pk>', views.ShelfDetail.as_view()),
    path('product_sizes/', views.ProductSizeList.as_view()),
    path('product_sizes/<int:pk>', views.ProductSizeDetail.as_view()),
    path('product_locations/', views.ProductLocationList.as_view()),
    path('product_locations/<int:pk>', views.ProductLocationDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
