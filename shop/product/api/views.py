from rest_framework import views
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import ProductSerializer,CategorySerializer
from ..models import Product, Category


class ProductViewSet(ModelViewSet): 
    queryset = Product.undeleted_objects.all()
    serializer_class = ProductSerializer


class CategorytViewSet(ModelViewSet): 
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request):
        queryset = Category.objects.filter(parent__isnull=True)
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)