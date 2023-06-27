from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import time

from products.forms import ProductCreateForm, CategoryCreateForm
from products.models import Product, Category


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

def category_list_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'products/categories.html', context=context)

def products_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        context = {
            'product': product
        }
        return render(request, 'products/detail.html', context=context)


def product_create_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm()
        }
        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        data = request.POST
        file = request.FILES

        form = ProductCreateForm(data, file)

        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get('image'),
                name=form.cleaned_data.get('name'),
                quantity=form.cleaned_data.get('quantity'),
                description=form.cleaned_data.get('description')
            )

            return redirect('/products/')

        return render(request, 'products/create.html', context={
            'form': form
        })


def category_create_view(request):
    if request.method == 'GET':
        context = {
            'form': CategoryCreateForm()
        }
        return render(request, 'products/categories.html', context=context)

    if request.method == 'POST':
        data = request.POST

        form = CategoryCreateForm(data)

        if form.is_valid():
            Category.objects.create(
                title=form.cleaned_data.get('title')
            )

            return redirect('/categories/')

        return render(request, 'products/categories.html', context={
            'form': form
        })
