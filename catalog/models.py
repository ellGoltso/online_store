from django.db import models
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Категория", help_text="Введите категорию"
    )
    description = models.TextField(verbose_name="Описание категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Продукт",
    )
    description = models.TextField(verbose_name="Описание продукта")
    image = models.ImageField(
        upload_to="catalog/photo", blank=True, null=True, verbose_name="Изображение"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="products",
    )
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения", auto_now=True
    )
    publication_status = models.BooleanField(verbose_name="Статус публикации", default=False)
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        related_name="products",
        default=None,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

        ordering = ["name", "category", "price"]
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
        ]
