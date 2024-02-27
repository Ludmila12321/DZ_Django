from django.contrib import admin
from .models import Category, Product, Client, Order, OrderProduct


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

    readonly_fields = ['date_added', 'rating']
    fieldsets = [(None, {'classes': ['wide'], 'fields': ['name'], }, ), ('Подробности', {'classes': ['collapse'], 'description': 'Категория товара и его подробное описание', 'fields': ['category', 'description'], },),
                 ('Бухгалтерия', {'fields': ['price', 'quantity'], }), ('Рейтинг и прочее', {'description': 'Рейтинг сформирован автоматически на основе оценок покупателей', 'fields': ['rating', 'date_added'], }),]


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address', 'registration_date']
    list_filter = ['registration_date']
    search_fields = ['name', 'email']
    ordering = ['registration_date']
    readonly_fields = ['registration_date']

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_amount', 'order_date']
    list_filter = ['order_date']
    search_fields = ['client__name']
    ordering = ['-order_date']
    readonly_fields = ['order_date']
    inlines = [OrderProductInline]


admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
