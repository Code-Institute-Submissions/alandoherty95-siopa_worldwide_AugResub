from django.contrib import admin
from .models import Product, Category


# ADMIN PRODUCT VIEW
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'image',
    )

    ordering = ('name',)


# ADMIN CATEGORY VIEW
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
