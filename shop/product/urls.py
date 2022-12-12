from django.urls import include, path
from django.views.generic import TemplateView
from .views import ProductListView

app_name='product'
urlpatterns = [
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('shop/', ProductListView.as_view(), name='shop'),
    path('product-sale/', TemplateView.as_view(template_name='product/product-sale.html'), name='product-sale'),
]
