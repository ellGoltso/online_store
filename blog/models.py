from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок', help_text='Введите заголовок')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/photo', blank=True, null=True, verbose_name="Изображение")
    date_of_publication = models.DateField(verbose_name="Дата публикации", auto_now_add=True)
    publication_sign = models.BooleanField(verbose_name="Признак публикации")
    number_of_views = models.IntegerField(verbose_name="Количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блоговая запись"
        verbose_name_plural = "Блоговые записи"

        ordering = ["title", "date_of_publication"]

    # заголовок,
    # содержимое,
    # превью(изображение),
    # дата
    # создания,
    # признак
    # публикации(булевое
    # поле),
    # количество
    # просмотров.
