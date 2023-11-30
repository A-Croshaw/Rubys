from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Creates Admin For The Products
    """
    list_display = (
        'sku',
        'ISBN',
        'author',
        'title',
        'pages',
        'this_edition',
        'condtion',
        'language',
        'price',
        'rating',
    )

    ordering = ('sku',)
    
class CategoryAdmin(admin.ModelAdmin):
    """
    Creates Admin For The Catergorys
    """
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
