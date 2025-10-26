from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = "Add test products to the database"

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.create(
            name="test_category", description="category description"
        )
        category = Category.objects.get(name="test_category")
        Product.objects.create(
            name="test_product", description="tedt_desc", price=25000, category=category
        )