from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'product/shop.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self, **kwargs):
        slug = self.kwargs.get('slug')
        if slug:
            category = get_object_or_404(Category, slug=slug)
            categories = category.get_children()
            return Product.undeleted_objects.filter(category__in =categories)
        else:
            return Product.undeleted_objects.all()


class ProducOfferListView(ListView):
    model = Product
    template_name = 'product/shop.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self, **kwargs):
        product = Product.undeleted_objects.filter(discount__isnull =False)
        return product


class ProductSearchListView(ListView):
    model = Product
    template_name = 'product/shop.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self, **kwargs):
        search = self.request.GET.get('search')
        if search:
            self.request.session['search'] = search
        else:
            try:
                search = self.request.session['search'] 
            except:
                search = ''
            
        product1 = Product.undeleted_objects.filter(title__contains =search)
        product2 = Product.undeleted_objects.filter(content__contains =search)
        product = product1 | product2
        return product



class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product.html'
    context_object_name = 'product' 


    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        product = kwargs.get('object')
        print(5555555555555555555, product.comments.filter(status = 2))
        context['comments'] =  product.comments.filter(status = 2)
        return context
