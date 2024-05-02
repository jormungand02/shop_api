from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(ProductImage)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'description', 'created', 'image')
    list_filter = ('created',)
    search_fields = ('name', 'category')