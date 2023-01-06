from django.urls import path,include
from .views import CheckOutAPIView, OrderPayView, OrderCustomerAPIView,OrderViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register('orders', OrderViewSet)

app_name='order'
urlpatterns = [
    path('', include((router.urls))),
    path('checkout/', CheckOutAPIView.as_view(), name='checkout'),
    path('order-pay/<int:order_id>/', OrderPayView.as_view(), name='order-pay'),
    path('customer-order-list/', OrderCustomerAPIView.as_view(), name='customer-order-list'),
]
