from rest_framework import serializers
from ..models import Product, Category, Gallery, Image, Property


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategorySerializer(serializers.ModelSerializer):
    childrens = RecursiveField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'parent', 'title', 'slug', 'content',
                  'image', 'is_navbar', 'get_absolute_url', 'childrens')


class SimpleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'parent', 'title', 'slug', 'content',
                  'is_navbar', 'get_absolute_url')


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'key', 'value', 'product')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'gallery', 'image_alt', 'image', 'name')


class GalerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id', 'product', 'main_pic', 'name', 'images')
    images = ImageSerializer(many=True)


class ProductSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Product
        fields = ('id', 'category', 'user', 'title', 'slug',
                  'is_shop', 'warehouse_code', 'discount',
                  'quantity', 'published_at', 'starts_at',
                  'ends_at', 'content', 'brand',
                  'get_absolute_url', 'is_new',
                  'average_rating', 'get_after_discount_price',
                  'get_last_price', 'galery', 'property'
                  )
    category = SimpleCategorySerializer()
    galery = GalerySerializer(required=False)
    property = PropertySerializer(many=True, required=False)
