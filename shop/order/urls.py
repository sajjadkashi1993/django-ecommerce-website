from django.urls import path
from .views import ChackOutView

app_name = 'order'
urlpatterns = [
    path('checkout/', ChackOutView.as_view(), name='checkout'),
]
