from django.urls import include, path
from .views import ProductViewSet, CategorytViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products',ProductViewSet )
router.register('categories',CategorytViewSet )
app_name='product'


# urlpatterns = router.urls
# 


urlpatterns = [
    path('', include((router.urls, 'product'), namespace='products')),
]
