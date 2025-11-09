from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    ProductCreateView,
    ProductListView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    UnpublishProductView,
    CategoryListView,
    ProductOfCategoryView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("new/", ProductCreateView.as_view(), name="product_create"),
    path("", ProductListView.as_view(), name="product_list"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path(
        "<int:pk>/unpublish/", UnpublishProductView.as_view(), name="product_unpublish"
    ),
    path("category/", CategoryListView.as_view(), name="category_list"),
    path(
        "category/<int:pk>/",
        ProductOfCategoryView.as_view(),
        name="products_of_category",
    ),
]
