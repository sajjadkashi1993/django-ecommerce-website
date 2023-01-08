from rest_framework import serializers
from ..models import Product, Category, Gallery, Image, Property, Price


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
        fields = ('id', 'key', 'value')

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Property.objects.create(product_id=product_id, **validated_data)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image_alt', 'image', 'name')


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('id', 'amount', 'created_at')

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Price.objects.create(product_id=product_id, **validated_data)


class GalerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id', 'main_pic', 'name', 'images')
    images = ImageSerializer(many=True)


class ProductFullSerializer(serializers.ModelSerializer):
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


class ProductSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'get_after_discount_price',
                  'main_pic', 'get_absolute_url')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'category', 'user', 'title', 'slug',
                  'is_shop', 'warehouse_code', 'discount',
                  'quantity', 'published_at', 'starts_at',
                  'ends_at', 'content', 'brand',
                  'galery', 'property', 'prices'
                  )
    property = PropertySerializer(many=True, read_only=True)
    galery = GalerySerializer(required=False, read_only=True)
    prices = PriceSerializer(many=True, read_only=True)

    # def create(self, validated_data):
    #     properteis_data = validated_data.pop('property')
    #     # galery_data = validated_data.pop('galery')
    #     prices_data = validated_data.pop('prices')
    #     product = Product.objects.create(**validated_data)
    #     # images_data = galery_data.pop('images')
    #     # galery = Gallery(product=product,**galery_data)
    #     # for image_data in images_data:
    #     #     Image.objects.create(galery=galery,**image_data)
    #     for property_data in properteis_data:
    #         Property.objects.create(product=product,**property_data)
    #     for price_data in prices_data:
    #         Price.objects.create(product=product, **price_data)
    #     return product

    # def update(self, instance, validated_data):
    #     properteis_data = validated_data.pop('property')
    #     prices_data = validated_data.pop('prices')

    #     property = instance.property.all()
    #     for item in properteis_data:
    #         for k, v in item_data.items():
    #             setattr(item, k, v)
    #             item.save()
