from django.urls import path
from . import views

urlpatterns = [
    path('ordered-products/7/', views.ordered_products, {'days': 7}, name='ordered_products_7'),
    path('ordered-products/30/', views.ordered_products, {'days': 30}, name='ordered_products_30'),
    path('ordered-products/365/', views.ordered_products, {'days': 365}, name='ordered_products_365'),
]