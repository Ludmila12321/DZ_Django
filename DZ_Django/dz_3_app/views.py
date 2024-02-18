from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Order

def ordered_products(request, days):
    today = datetime.now().date()
    start_date = today - timedelta(days=days)
    ordered_products = Order.objects.filter(order_date__range=[start_date, today])
    
    ordered_products_list = []
    unique_products = set()
    for order in ordered_products:
        for product in order.products.all():
            if product not in unique_products:
                ordered_products_list.append(product)
                unique_products.add(product)
    
    context = {
        'ordered_products': ordered_products_list,
        'days': days
    }
    return render(request, 'ordered_products.html', context)