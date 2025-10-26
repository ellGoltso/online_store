from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class Command(BaseCommand):
    help = "Add test products and group to the database"

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.create(
            name="Инструменты", description="Инструменты для ремонта"
        )
        category = Category.objects.get(name="Инструменты")
        tools = [
            {"name": "Стамеска", "description": "Стамеска для работы по дереву", "price": 1000, "category": category},
            {"name": "Рулетка", "description": "Для измерения размеров", "price": 500, "category": category},
            {"name": "Молоток", "description": "Для забивания гвоздей", "price": 800, "category": category},
        ]
        for tool in tools:
            product = Product.objects.create(**tool)
            self.stdout.write(self.style.SUCCESS(f'Successfully added tool: {product.name}'))

        product_moderator_group = Group.objects.create(name='Модератор продуктов')
        can_unpublish_product_permission = Permission.objects.get(codename='can_unpublish_product')
        delete_product_permission = Permission.objects.get(codename='delete_product')

        product_moderator_group.permissions.add(can_unpublish_product_permission, delete_product_permission)
