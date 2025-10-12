from django.shortcuts import render
from catalog.models import Product

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)

def contacts(request):
    return render(request, 'contacts.html')

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

# def list_products(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, '')