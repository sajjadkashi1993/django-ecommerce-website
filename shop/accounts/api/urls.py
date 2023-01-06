from django.urls import path
from .views import AddressCustomerAPIView


app_name='accounts'
urlpatterns = [
    path('customer-adderss-list/', AddressCustomerAPIView.as_view(), name='customer-adderss-list'),
    
]
