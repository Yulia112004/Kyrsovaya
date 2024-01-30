from django.contrib import admin

# Register your models here.
from catalog.models import Product, Category, Contact, Version

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('product_name', 'product_disc',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'country', 'inn', 'address',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version_number', 'product')
    list_filter = ('is_active',)