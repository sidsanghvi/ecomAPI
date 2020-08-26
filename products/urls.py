from django.urls import path
from .views import *

urlpatterns = [
    path("products/", product_list, name='product-list'),
    path('products/<int:pk>', product_detail, name='producr-detail'),
]
