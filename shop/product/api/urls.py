from django.urls import include, path
from .views import productApiViews

app_name='product'
urlpatterns = [
    path('shop/', productApiViews.as_view(), name='products'),
]
