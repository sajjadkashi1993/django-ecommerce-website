from django.db import models
from core.models import BaseModel
from django.contrib.auth import get_user_model
from discount.models import Coupon
from product.models import Product
User = get_user_model()

# Create your models here.


class Order(BaseModel):
    """
        Id:	The unique id to identify the order.
        User: The user id to identify the user or buyer associated with the order.
        Status:	The status of the order can be New, Checkout, Paid, Failed, Shipped, Delivered, Returned, and Complete.
        Sub Total:	The total price of the Order Items.
        Discount The total discount of the Order Items.
        Tax: The tax on the Order Items.
        Shipping: The shipping charges of the Order Items.
        Total: The total price of the Order including tax and shipping. It excludes the items discount.
        coupon: 
        Discount: The total discount of the Order based on the promo code or store discount.
        Grand Total: The grand total of the order to be paid by the buyer.
        Receiver Name: The first name of the user.
        Receiver Mobile:	The mobile number of the user.
        Province: The province of the address.
        City: The city of the address.
        Address: The body of the address.
        Created At:	It stores the date and time at which the order is created.
        Updated At:	It stores the date and time at which the order is updated.
        Content:	The column used to store the additional details of the order.
    """
    class STATUS(models.IntegerChoices):
        """
            This is a class for status choices.
        """
        New = 1, 'New'
        Checkout = 2, 'Checkout'
        Paid = 3, 'Paid'
        Failed = 4, 'Failed'
        Shipped = 5, 'Shipped'
        Delivered = 6, 'Delivered'
        Returned = 7, 'Returned'
        Complete = 8, 'Complete'

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders')
    status = models.IntegerField(choices=STATUS.choices, default=STATUS.New)
    coupon = models.ForeignKey(
        Coupon, on_delete=models.SET_NULL, related_name='orders', null=True, blank=True)
    sub_total = models.DecimalField(max_digits=20, decimal_places=2)
    tax = models.DecimalField(max_digits=20, decimal_places=2)
    shipping = models.DecimalField(max_digits=20, decimal_places=2)
    total = models.DecimalField(max_digits=20, decimal_places=2)
    discount = models.DecimalField(max_digits=20, decimal_places=2)
    grand = models.DecimalField(max_digits=20, decimal_places=2)
    receiver_name = models.CharField(max_length=100)
    receiver_mobile = models.CharField(max_length=15)
    country = models.CharField(max_length=100, default='iran')
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.user}, {self.id}'


class OrderItem(BaseModel):
    """
        Id:	The unique id to identify the ordered item.
        Product:	The product id to identify the product associated with the ordered item.
        Order:	The order id to identify the order associated with the ordered item.
        Warehouse code:	The warehouse code of the product while purchasing it.
        Price:	The price of the product while purchasing it.
        Discount:	The discount of the product while purchasing it.
        Quantity:	The quantity of the product selected by the user.
        Created At:	It stores the date and time at which the ordered item is created.
        Updated At:	It stores the date and time at which the ordered item is updated.
    """
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name='order_items')
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')
    warehouse_code = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    discount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'{self.product}:{self.quantity}'


class Transaction(BaseModel):
    """
        Id:	The unique id to identify the transaction.
        User:	The user id to identify the user associated with the transaction.
        Order:	The order id to identify the order associated with the transaction.
        Code:	The payment id provided by the payment gateway.
        Status:	The status of the order transaction can be New, Cancelled, Failed, Pending, Declined, Rejected, and Success.
        Created At:	It stores the date and time at which the order transaction is created.
        Updated At:	It stores the date and time at which the order transaction is updated.
        Content:	The column used to store the additional details of the transaction.
    """
    class STATUS(models.IntegerChoices):
        New = 1, 'New'
        Cancelled = 2, 'Cancelled'
        Failed = 3, 'Failed'
        Pending = 4, 'Pending'
        Declined = 5, 'Declined'
        Rejected = 6, 'Rejected'
        Success = 7, 'Success'

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='transactions')
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='transactions')
    code = models.CharField(max_length=50)
    status = models.IntegerField(choices=STATUS.choices, default=STATUS.New)
    content = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.order}:{self.code}'
