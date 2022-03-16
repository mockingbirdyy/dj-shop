from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sub_category', 'is_sub')



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'author','price', 'available')
    raw_id_fields = ('category',)