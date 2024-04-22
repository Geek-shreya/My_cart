from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nslides = n//4 + ceil((n/4) - (n//4))
    
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4) - (n//4))
        allProds.append([prod, range(1,nslides), nslides])
    params = { 'allProds' : allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request):
    return render(request, 'shop/productView.html')

def checkout(request):
    return render(request, 'shop/checkout.html')
   

