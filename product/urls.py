

from django.urls import path, include 

from rest_framework.routers import DefaultRouter

from product.views import ProductAPI, TotalSalesAPI

product_router = DefaultRouter() 
product_router.register(r'products', ProductAPI, basename='product')
product_router.register(r'total_sales', TotalSalesAPI, basename='total_sales')


urlpatterns = [ 
    path('', include(product_router.urls))
]