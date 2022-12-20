from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse

from comment.forms import CommentForm
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
        context['comments'] =  product.comments.filter(status = 2, is_reply=False)
        context['related_product'] = Product.undeleted_objects.filter(category=product.category)[:3]
        return context


    def post(self, request,**kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.product = Product.undeleted_objects.get(pk=kwargs['pk'])
            if request. user.is_authenticated:
                new_comment.user = request.user
            new_comment.save()
            return JsonResponse({'msg':'Your comment sended', 'status':'success'}, status=201)
        return JsonResponse(form.errors, status=400)
        