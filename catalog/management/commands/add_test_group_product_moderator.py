from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from users.models import CustomUser


class Command(BaseCommand):
    help = "Add test products and group to the database"

    def handle(self, *args, **options):

        user, created = CustomUser.objects.get_or_create(
            email="test_user_5@mail.ru", username="test_user_5", password="12345678gf"
        )
        user1, created = CustomUser.objects.get_or_create(
            email="test_user_7@mail.ru", username="test_user_7", password="12345678"
        )
        Category.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.create(
            name="Инструменты", description="Инструменты для ремонта"
        )
        category = Category.objects.get(name="Инструменты")
        tools = [
            {
                "name": "Стамеска",
                "description": "Стамеска для работы по дереву",
                "price": 1000,
                "category": category,
                "publication_status": True,
                "owner": user,
            },
            {
                "name": "Рулетка",
                "description": "Для измерения размеров",
                "price": 500,
                "category": category,
                "publication_status": True,
                "owner": user,
            },
            {
                "name": "Молоток",
                "description": "Для забивания гвоздей",
                "price": 800,
                "category": category,
                "publication_status": True,
                "owner": user,
            },
        ]
        for tool in tools:
            product = Product.objects.create(**tool)
            self.stdout.write(
                self.style.SUCCESS(f"Successfully added tool: {product.name}")
            )

        product_moderator_group, created = Group.objects.get_or_create(
            name="Модератор продуктов"
        )
        can_unpublish_product_permission = Permission.objects.get(
            codename="can_unpublish_product"
        )
        delete_product_permission = Permission.objects.get(codename="delete_product")

        product_moderator_group.permissions.add(
            can_unpublish_product_permission, delete_product_permission
        )
        user.groups.add(product_moderator_group)
