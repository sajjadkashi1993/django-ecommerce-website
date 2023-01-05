from django.urls import path
from .views import ChackOutView, OrderVerifyView
from django.views.generic import TemplateView
app_name = 'order'
urlpatterns = [
    path('checkout/', ChackOutView.as_view(), name='checkout'),
    path('order-verify/', OrderVerifyView.as_view(), name='order-verify'),
    path('order-pay/', TemplateView.as_view(template_name='order/pay.html'), name='order-pay'),
]
