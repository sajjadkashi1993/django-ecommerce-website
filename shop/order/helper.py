from order.api.serializers import OrderItemSerilizers
from .models import Order


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
                checked= False
                msg.append(f'Only {item.product.quantity} of the {item.product.title} are left.')
        return((checked, msg))

    def add_order_items(self, cart):
          for item in cart.cart_items.all():
            if item.product.quantity - item.quantity < 0:
                raise Exception
            data= {
                'product':item.product.id,
                'order':self.order.id,
                'warehouse_code':item.product.warehouse_code,
                'price':item.product.get_after_discount_price(),
                'quantity':item.quantity,
            }

            order_item = OrderItemSerilizers(data=data)
            if order_item.is_valid():
                order_item.save()