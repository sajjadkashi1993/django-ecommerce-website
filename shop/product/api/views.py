from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PropertySerializer, ProductFullSerializer,CategorySerializer, ProductSerializer
from ..models import Product, Category, Property
from .filters import ProductFilter

class CategorytViewSet(ModelViewSet): 
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request):
        queryset = Category.objects.filter(parent__isnull=True)
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

class ProductListFullView(generics.ListAPIView): 
    queryset = Product.undeleted_objects.all()
    serializer_class = ProductFullSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = ProductFilter
    search_fields = ['title', 'warehouse_code', 'content', 'brand']
    ordering_fields = ['title']
    pagination_class = PageNumberPagination

class ProductRetrievFullView(generics.RetrieveAPIView): 
    queryset = Product.undeleted_objects.all()
    serializer_class = ProductFullSerializer


class ProductViewSet(ModelViewSet): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class  PropertyViewSet(ModelViewSet): 
    serializer_class = PropertySerializer

    def get_queryset(self):
        return Property.objects.filter(product=self.kwargs['product_pk'])






        