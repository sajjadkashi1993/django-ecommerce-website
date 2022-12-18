from django.urls import path
from .views import ProductListView, ProductDetailtView,ProductSearchListView,ProducOfferListView

app_name = 'product'
urlpatterns = [
    path('shop/', ProductListView.as_view(), name='shop'),
    path('shop/search/', ProductSearchListView.as_view(), name='search'),
    path('shop/offer/', ProducOfferListView.as_view(), name='offer'),
    path('shop/<str:slug>', ProductListView.as_view(), name='cat'),
    path('<int:pk>/', ProductDetailtView.as_view(), name='product'),
]
