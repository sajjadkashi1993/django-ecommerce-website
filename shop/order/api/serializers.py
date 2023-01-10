from rest_framework import serializers
from ..models import Order, OrderItem


class OrderItemSerilizers(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerilizers(serializers.ModelSerializer):
    items = OrderItemSerilizers(many=True, read_only=True)
    status = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%b %d %Y %H:%M", read_only=True)
    class Meta:
        model = Order
        fields = ('id', 'created_at', 'user', 'status', 'coupon', 'sub_total', 'tax', 'shipping', 'total', 'discount', 'grand', 'receiver_name', 'receiver_mobile', 'country', 'province', 'city', 'address', 'postal_code', 'content', 'items')

    def get_status(self,obj:Order):
        return obj.get_status_display()
