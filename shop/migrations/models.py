from django.db import models


class Product(models.Model):

    CATEGORY_CHOICES = [
        ('hoodies', 'Худі'),
        ('tshirts', 'Футболки'),
        ('shirts', 'Сорочки'),
        ('jeans', 'Джинси'),
        ('jackets', 'Куртки'),
        ('accessories', 'Аксесуари'),
    ]

    name = models.CharField(
        max_length=200,
        verbose_name='Назва товару'
    )

    description = models.TextField(
        verbose_name='Опис товару'
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Ціна'
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        verbose_name='Категорія'
    )

    size = models.CharField(
        max_length=50,
        verbose_name='Розмір'
    )

    color = models.CharField(
        max_length=50,
        verbose_name='Колір'
    )

    image = models.ImageField(
        upload_to='products/',
        verbose_name='Фото товару'
    )

    stock = models.PositiveIntegerField(
        default=0,
        verbose_name='Кількість на складі'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата додавання'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        ordering = ['-created_at']
