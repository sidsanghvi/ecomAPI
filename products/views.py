from django.shortcuts import render
from django.http import JsonResponse

from .models import *
# Create your views here.


def product_list(request):
    products = Product.objects.all()
    data = {'products': list(products.values())}
    response = JsonResponse(data)
    return response


def product_detail(reauest, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {'product': {
            'name': product.name,
            'manufacturer': product.manufacturer.name,
            'description': product.description,
            'photo': product.photo.url,
            'price': product.price,
            'shipping cost': product.shipping_cost,
            'quantity': product.quantity
        }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            'error': {
                'code': 404,
                'message': 'product not found'
            }},
            status=404)
    return response
