from django.urls import include, path
from .views import PriceViewSet, PropertyViewSet, ProductViewSet, CategorytViewSet, ProductListFullView, ProductRetrievFullView
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
router = routers.DefaultRouter()
router.register('categories', CategorytViewSet)
router.register('products', ProductViewSet)

product_routers = routers.NestedDefaultRouter(router,'products',lookup='product' )
product_routers.register('proprty',PropertyViewSet, basename='product-proprty')
product_routers.register('price',PriceViewSet, basename='product-price')

app_name = 'product'
urlpatterns = [
    path('', include((router.urls, 'product'), namespace='products')),
    path('', include((product_routers.urls))),
    path('full-detail/', ProductListFullView.as_view() , name='full-detail-list'),
    path('full-detail/<int:pk>/', ProductRetrievFullView.as_view() , name='full-detail'),
]
