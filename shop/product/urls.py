from django.urls import path
from .views import ProductListView, ProductDetailtView

app_name = 'product'
urlpatterns = [
    path('shop/', ProductListView.as_view(), name='shop'),
    path('shop/<str:slug>', ProductListView.as_view(), name='cat'),
    path('<int:pk>/', ProductDetailtView.as_view(), name='product'),
]
