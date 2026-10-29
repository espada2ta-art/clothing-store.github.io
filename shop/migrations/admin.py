from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'category',
        'price',
        'size',
        'color',
        'stock',
        'created_at',
    )

    list_filter = (
        'category',
        'size',
        'color',
    )

    search_fields = (
        'name',
        'description',
    )

    ordering = (
        '-created_at',
    )
