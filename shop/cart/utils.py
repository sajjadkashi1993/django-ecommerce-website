from product.models import Product
from product.api.serializers import ProductSimpleSerializer
from decimal import Decimal
from .models import CartItem
from django.db import IntegrityError

def session_cart(data: dict)-> dict:
    cart_item = []
    grand_total = 0
    for k, v in data.items():
        product = Product.undeleted_objects.get(id=k)
        serilized_product = ProductSimpleSerializer(product).data
        sub_total = Decimal(
            serilized_product['get_after_discount_price']) * Decimal(v)
        grand_total += sub_total
        cart_item.append({'product': serilized_product,
                         'quantity': v, 'sub_total': sub_total})
    return {'cart_items': cart_item, 'grand_total': grand_total}


def add_session_cart(user, cart_session:dict):
    cart = user.carts.get_or_create(user=user, status=2)[0]
    for k,v in cart_session.items():
        product = Product.undeleted_objects.get(id=k)
        try:
            cart_item = CartItem.objects.create(
                cart=cart, product=product, quantity=v)
        except IntegrityError:
            cart_item = CartItem.objects.get(cart=cart, product=product)
            cart_item.quantity = v
            cart_item.save()
