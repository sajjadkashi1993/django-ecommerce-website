from django.shortcuts import render
from django.views.generic.list import ListView, BaseListView
from .models import Product
# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
