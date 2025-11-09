from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView, View
from catalog.models import Product, Category
from catalog.forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden, Http404
from .services import ProductService
from django.core.cache import cache


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        user = self.request.user
        if user.groups.filter(name="Модератор продуктов").exists() or obj.owner == user:
            return obj
        else:
            raise Http404("У Вас нет прав для редактирования данного продукта.")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    permission_required = ("catalog.delete_product",)
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        user = self.request.user
        is_in_group = False
        for group in user.groups.all():
            if group.name == "Модератор продуктов":
                is_in_group = True
                break
        if is_in_group or obj.owner == user:
            return obj
        else:
            raise Http404("У Вас нет прав для удаления данного продукта.")


class ProductListView(ListView):
    model = Product
    template_name = "catalog/index.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = cache.get("products_queryset")
        if not queryset:
            queryset = super().get_queryset()
            cache.set(
                "products_queryset", queryset, 60 * 15
            )  # Кешируем данные на 15 минут
        return queryset


@method_decorator(cache_page(60 * 15), name="dispatch")
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if not request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponseForbidden(
                "У вас нет прав для отмены публикации продукта."
            )

        product.publication_status = False
        product.save()

        return redirect("catalog:product_list")


class CategoryListView(ListView):
    model = Category
    template_name = "catalog/categories_list.html"
    context_object_name = "categories"


class ProductOfCategoryView(DetailView):
    model = Category
    template_name = "catalog/products_of_category.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_category = self.object.id
        context["products_by_category"] = ProductService.get_products_of_category(
            product_category
        )
        return context
