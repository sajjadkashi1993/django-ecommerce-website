from django.urls import path
from .views import AddressCustomerAPIView, AddressCustomerListAPIView


app_name = 'accounts'
urlpatterns = [
    path('customer-adderss-list/', AddressCustomerListAPIView.as_view(),
         name='customer-adderss-list'),
    path('customer-adderss/<int:pk>/',
         AddressCustomerAPIView.as_view(), name='customer-adderss'),

]
