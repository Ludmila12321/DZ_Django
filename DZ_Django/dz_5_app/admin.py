from django.contrib import admin
from .models import Category, Product

@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'quantity']
    ordering = ['category', '-quantity']
    list_filter = ['date_added', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)