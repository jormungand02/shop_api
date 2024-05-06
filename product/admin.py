from django.contrib import admin

from .models import Product, Category, ProductImage

admin.site.register(Category)
admin.site.register(ProductImage)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created', 'image')
    list_filter = ('created',)
    search_fields = ('name', 'category')