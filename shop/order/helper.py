from time import sleep
from order.api.serializers import OrderItemSerilizers
from order.exceptions import QuantityOrderException
from .models import Order
from product.models import Product
from django.db import IntegrityError, transaction


class OrderHelper():

    def __init__(self, order) -> None:
        self.order = order

    def check_order(self):
        checked = True
        # if self.order.grand <= 1:
        #     checked = False
        #     msg= 'The order amount must be more than $1.'
        #     return((checked, msg))
        msg = []
        for item in self.order.items.all():
            if item.product.quantity - item.quantity < 0:
                checked = False
                msg.append(
                    f'Only {item.product.quantity} of the {item.product.title} are left.')
        return ((checked, msg))

    def add_order_items(self, cart):
        for item in cart.cart_items.all():
            if item.product.quantity - item.quantity < 0:
                raise QuantityOrderException(
                    f'There are only {item.product.quantity} left of {item.product.title}. You have ordered {item.quantity} pieces.')
            data = {
                'product': item.product.id,
                'order': self.order.id,
                'warehouse_code': item.product.warehouse_code,
                'price': item.product.get_after_discount_price(),
                'quantity': item.quantity,
            }

            order_item = OrderItemSerilizers(data=data)
            if order_item.is_valid():
                order_item.save()

    def operation_after_payment(self, request):
        self.order.status = 3 #Paid
        self.order.save()
        user = request.user
        cart = user.carts.get(user=user, status=2)
        cart.status = 1 # ordered
        cart.save()
        with transaction.atomic():
            order_items = self.order.items.select_related('product').select_for_update()
            for item in order_items:
                product = item.product
                product.quantity = product.quantity - item.quantity
                try:
                    product.save()
                except IntegrityError as e:
                    print(4444444444444,e)


