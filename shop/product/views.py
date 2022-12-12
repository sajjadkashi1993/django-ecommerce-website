from django.shortcuts import render
from django.views.generic.list import ListView, BaseListView
from .models import Product, Category
# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'product/shop.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_navbar = True)
        return context