from django.urls import path
from .views import CheckOutAPIView, OrderPayView

app_name='order'
urlpatterns = [
    path('checkout/', CheckOutAPIView.as_view(), name='checkout'),
    path('order-pay/<int:order_id>/', OrderPayView.as_view(), name='order-pay'),
]
