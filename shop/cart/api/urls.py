from django.urls import path
from .views import AddToCart, ShowCart, DelCart

app_name='cart'
urlpatterns = [
    path('add/', AddToCart.as_view(), name='add-to-cart'),
    path('show/', ShowCart.as_view(), name='show-cart'),
    path('del/', DelCart.as_view(), name='delete-cart'),
]
