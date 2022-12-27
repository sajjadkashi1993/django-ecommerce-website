from django.urls import include, path
from .views import CategorytViewSet, ProductListFullView, ProductRetrievFullView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categories', CategorytViewSet)
app_name = 'product'


urlpatterns = [
    path('', include((router.urls, 'product'), namespace='products')),
    path('full-detail/', ProductListFullView.as_view() , name='full-detail-list'),
    path('full-detail/<int:pk>/', ProductRetrievFullView.as_view() , name='full-detail'),
]
