from .models import Product, Category


class ProductService:

    @staticmethod
    def get_products_of_category(category_id) -> None | list[Product]:
        """Возвращает список всех продуктов в указанной категории"""

        category = Category.objects.get(id=category_id)
        products = Product.objects.filter(category=category)
        if not products.exists():
            return None
        return products
