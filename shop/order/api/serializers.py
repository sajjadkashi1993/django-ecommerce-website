from rest_framework import serializers
from ..models import Order, OrderItem


class OrderItemSerilizers(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
  