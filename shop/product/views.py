from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q

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
            return Product.undeleted_objects.filter(category__in=categories)
        else:
            return Product.undeleted_objects.all()


class ProducOfferListView(ListView):
    model = Product
    template_name = 'product/shop.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self, **kwargs):
        product = Product.undeleted_objects.filter(discount__isnull=False)
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

        product = Product.undeleted_objects.filter(Q(title__contains=search) | Q(content__contains=search))

        return product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        product = kwargs.get('object')
        context['comments'] = product.comments.filter(status=2, is_reply=False)
        context['related_product'] = Product.undeleted_objects.filter(
            category=product.category).exclude(id=product.id)[0:4]
        return context
