from django.shortcuts import render
from django.views.generic.list import ListView, BaseListView
from .models import Product
# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'product/shop.html'
    context_object_name = 'products'
