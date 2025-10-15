# from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from catalog.models import Product

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'image', 'category', 'price']
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'image', 'category', 'price']
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy('catalog:product_list')

class ProductListView(ListView):
    model = Product
    template_name = "catalog/index.html"
    context_object_name = "products"

class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"

#
# def home(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'index.html', context)
#
# def contacts(request):
#     return render(request, 'contacts.html')
#
# def product_detail(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     context = {'product': product}
#     return render(request, 'product_detail.html', context)
#
