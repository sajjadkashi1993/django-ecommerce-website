from django.db import models
from django.contrib.auth import get_user_model
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _
from product.models import Product

User = get_user_model()


class Cart(BaseModel):
    class Status(models.IntegerChoices):
        """
            This is a class for status choices.
        """
        ORDERED = 1, _('Ordered')
        NEW = 2, _('New')

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='carts')
    status = models.IntegerField(choices=Status.choices, default=Status.NEW)

    def __str__(self) -> str:
        return f'{self.user}:{self.status}'


class CartItem(BaseModel):
    class Status(models.IntegerChoices):
        """
            This is a class for status choices.
        """
        ACTIVE = 1, _('Active')
        DELETE = 2, _('Delete')

    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name='cart_items')
    quantity = models.PositiveIntegerField()
    status = models.IntegerField(choices=Status.choices, default=Status.ACTIVE)

    def __str__(self) -> str:
        return str(self.id)
