from rest_framework import serializers
from ..models import Order, OrderItem


class OrderItemSerilizers(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerilizers(serializers.ModelSerializer):
    # items = OrderItemSerilizers(many=True)
    status = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ('user', 'status', 'coupon', 'sub_total', 'tax', 'shipping', 'total', 'discount', 'grand', 'receiver_name', 'receiver_mobile', 'country', 'province', 'city', 'address', 'postal_code', 'content')

    def get_status(self,obj:Order):
        return obj.get_status_display()
