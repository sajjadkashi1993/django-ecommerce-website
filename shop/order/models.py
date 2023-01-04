from django.db import models
from core.models import BaseModel
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from discount.models import Coupon
from product.models import Product
from core.validators import PhoneValidator

User = get_user_model()
max_digits=settings.MAX_DIGITS
decimal_places=settings.DECIMAL_PLACES

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
        New = 1, _('New')
        Checkout = 2, _('Checkout')
        Paid = 3, _('Paid')
        Failed = 4, _('Failed')
        Shipped = 5, _('Shipped')
        Delivered = 6, _( 'Delivered')
        Returned = 7, _('Returned')
        Complete = 8, _('Complete')

    user = models.ForeignKey(
        User, on_delete=models.CASCADE,verbose_name=_('user'), related_name='orders')
    status = models.IntegerField(choices=STATUS.choices, default=STATUS.New)
    coupon = models.ForeignKey(
        Coupon, on_delete=models.SET_NULL,verbose_name=_('coupon'), related_name='orders', null=True, blank=True)
    sub_total = models.DecimalField(_('sub total'), max_digits=max_digits, decimal_places=decimal_places)
    tax = models.DecimalField(_('tax'), max_digits=max_digits, decimal_places=decimal_places)
    shipping = models.DecimalField(_('shipping'), max_digits=max_digits, decimal_places=decimal_places)
    total = models.DecimalField(_('total'), max_digits=max_digits, decimal_places=decimal_places)
    discount = models.DecimalField(_('discount'), max_digits=max_digits, decimal_places=decimal_places)
    grand = models.DecimalField(_('grand'), max_digits=max_digits, decimal_places=decimal_places)
    receiver_name = models.CharField(_('receiver name'), max_length=100)
    receiver_mobile = models.CharField(_('receiver mobile'), max_length=15, validators=[PhoneValidator()])
    country = models.CharField(_('country'), max_length=100, default='iran')
    province = models.CharField(_('province'), max_length=100)
    city = models.CharField(_('city'), max_length=100)
    address = models.CharField(_('address'), max_length=100)
    postal_code = models.CharField(_("postal code"), max_length=20)
    content = models.TextField(_('content'), null=True, blank=True)


    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _('orders')


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
        Product, on_delete=models.PROTECT,verbose_name=_('Product'), related_name='order_items')
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE,verbose_name=_('Order'), related_name='items')
    warehouse_code = models.CharField(_('warehouse code'), max_length=50)
    price = models.DecimalField(_('price'), max_digits=max_digits, decimal_places=decimal_places)
    quantity = models.PositiveIntegerField(_('quantity'), )


    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _('Order Items')


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
        New = 1, _('New')
        Cancelled = 2, _('Cancelled')
        Failed = 3, _('Failed')
        Pending = 4, _('Pending')
        Declined = 5, _('Declined')
        Rejected = 6, _('Rejected')
        Success = 7, _('Success')

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('user'), related_name='transactions')
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE,verbose_name=_('order'), related_name='transactions')
    code = models.CharField(_('code'), max_length=50)
    status = models.IntegerField(_('status'), choices=STATUS.choices, default=STATUS.New)
    content = models.TextField(_('content'), null=True, blank=True)


    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _('Transactions')

    def __str__(self) -> str:
        return f'{self.order}:{self.code}'
