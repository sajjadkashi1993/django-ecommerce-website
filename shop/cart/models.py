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

    user = models.ForeignKey(_('user'),
        User, on_delete=models.CASCADE, related_name='carts')
    status = models.IntegerField(_('status'),choices=Status.choices, default=Status.NEW)

    class Meta:
        verbose_name = _("cart")
        verbose_name_plural = _('carts')

    def __str__(self) -> str:
        return f'{self.user}: {self.status}'



class CartItem(BaseModel):
    class Status(models.IntegerChoices):
        """
            This is a class for status choices.
        """
        ACTIVE = 1, _('Active')
        DELETE = 2, _('Delete')

    cart = models.ForeignKey(_('cart'), 
        Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(_('product'), 
        Product, on_delete=models.PROTECT, related_name='cart_items')
    quantity = models.PositiveIntegerField(_('quantity'))
    status = models.IntegerField(_('status'), choices=Status.choices, default=Status.ACTIVE)

    def __str__(self) -> str:
        return str(self.id)
