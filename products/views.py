from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    featured_products = Product.objects.order_by('priority')[:3]
    latest_products = Product.objects.order_by('-id')[:3]
    context ={
        'featured_products': featured_products,
        'latest_products': latest_products
    }
    return render(request, 'index.html', context)

def list_products(request):
    """AI is creating summary for list_products
    return product list page

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    page = 1
    if request.GET:
        page = request.GET.get('page',1) # requesting to user , which page you need to show
        
    #   COLLECTING DATA FROM Products (from backend)
    product_list = Product.objects.order_by('priority')
    # pagenator object means it will seperate large amount of product items into diffrent items
    product_paginator = Paginator(product_list,2)
    product_list = product_paginator.get_page(page)
    #adding data into a dictnory
    context = {'products': product_list}
    return render(request, 'products.html', context)

def detail_product(request,pk):
    product = Product.objects.get(pk=pk)
    context ={'product':product}
    return render(request, 'product_detail.html', context)
