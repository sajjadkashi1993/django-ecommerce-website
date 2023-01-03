from decimal import Decimal
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from core.models import BaseModel
from django.utils.timezone import now
max_digits=settings.MAX_DIGITS
decimal_places=settings.DECIMAL_PLACES


class Coupon(BaseModel):
    code = models.CharField(_('code'), max_length=10)
    min_purchase = models.DecimalField(
        _('min purchase'), max_digits=max_digits, decimal_places=decimal_places)
    max_discount = models.DecimalField(
        _('max discount'), max_digits=max_digits, decimal_places=decimal_places)
    percent = models.PositiveSmallIntegerField(_('percent'))
    expire_time = models.DateTimeField(_('expire time'))
    limit_number = models.IntegerField(_('limit number'))
    start_time = models.DateTimeField(_('start time'))
    event = models.CharField(_('event'), max_length=100)

    class Meta:
        verbose_name = _("Coupon")
        verbose_name_plural = _('Coupons')

    def __str__(self) -> str:
        return self.code
    @property
    def is_active(self):
        if self.start_time < now() < self.expire_time and self.limit_number > 0:
            return True
        return False


    def is_min_purchase_ok(self, amount):
        if amount > self.min_purchase:
            return True
        return False

    def is_ok(self,request, amount):
        if self.is_active and self.is_min_purchase_ok(amount):
            if not request.user.orders.filter(coupon=self).exists():
                return True
        return False


    def apply_discount(self, amount):
        '''
        This method is for applying a discount on a specific amount.
        Returns the discount amount
        '''
        discount = round(amount * Decimal(self.percent/100),2)
        if discount > self.max_discount:
            discount = self.max_discount
        return discount
        
class Discount(BaseModel):
    class TYPE(models.IntegerChoices):
        percent = 1, 'Percent'
        amount = 2, 'Amount'

    type = models.IntegerField(_('type'), choices=TYPE.choices)
    percent = models.PositiveSmallIntegerField(
        _('percent'), null=True, blank=True)
    amount = models.DecimalField(_('amount'),
                                 max_digits=max_digits, decimal_places=decimal_places, null=True, blank=True)

    start_time = models.DateTimeField(_('start time'), )
    expire_time = models.DateTimeField(_('expire time'), )
    event = models.CharField(_('event'), max_length=100)

    class Meta:
        verbose_name = _("Discount")
        verbose_name_plural = _('Discounts')

    def __str__(self) -> str:
        if self.type == 1:
            return str(self.percent)+ '%'
        else :
            return str(self.amount)+ '$'
            
