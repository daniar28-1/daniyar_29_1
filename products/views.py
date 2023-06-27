from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import time

from products.models import Product


def helloview(request):
    if request.method == 'GET':
        return HttpResponse('Hello, its my first project')

def now_date(request):
    datetime = time()
    if request.method == 'GET':
        return HttpResponse(datetime)


def goodby(request):
    if request.method == 'GET':
        return HttpResponse('Goodby, user')


def main_view(request):
    if request.method == 'GET':
        return render(request,'layouts/index.html')

def products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'products/products.html', context=context)

