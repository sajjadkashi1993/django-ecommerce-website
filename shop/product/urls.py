from django.urls import include, path
from .views import ProductListView

app_name='product'
urlpatterns = [
    path('product-list/', ProductListView.as_view(), name='product-list'),
]
