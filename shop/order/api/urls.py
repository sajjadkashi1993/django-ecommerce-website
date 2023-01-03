from django.urls import path
from .views import CheckOutAPIView

app_name='order'
urlpatterns = [
    path('checkout/', CheckOutAPIView.as_view(), name='checkout'),
]
