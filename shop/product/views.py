from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product, Category
# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'product/shop.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self, **kwargs):
        # print(1111111111111111111, self.kwargs)
        slug = self.kwargs.get('slug')
        if slug:
            category = get_object_or_404(Category, slug=slug)
            categories = category.get_children()
            return Product.objects.filter(category__in =categories)
        else:
            return Product.objects.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_navbar = True)
        return context



class ProductDetailtView(DetailView):
    model = Product
    template_name = 'product/product.html'
    context_object_name = 'product' 