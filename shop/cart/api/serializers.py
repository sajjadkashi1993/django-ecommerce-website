from rest_framework import serializers
from ..models import Cart, CartItem
from product.api.serializers import ProductSimpleSerializer


class CartItemSerilizers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity', "sub_total"]

    product = ProductSimpleSerializer()
    sub_total = serializers.SerializerMethodField(method_name="total")

    def total(self, cartitem: CartItem):
        return cartitem.quantity * cartitem.product.get_after_discount_price()


class CartSerilizer(serializers.Serializer):
    class Meta:
        model = Cart
        fields = ['cart_items', "grand_total"]
    cart_items = CartItemSerilizers(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField(method_name='main_total')

    def main_total(self, cart: Cart):
        items = cart.cart_items.all()
        total = sum([item.quantity * item.product.get_after_discount_price()
                    for item in items])
        return total


