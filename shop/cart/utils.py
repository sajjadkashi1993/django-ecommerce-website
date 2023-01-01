from product.models import Product
from product.api.serializers import ProductSimpleSerializer
from decimal import Decimal


def session_cart(data: dict):
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
