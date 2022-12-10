from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from core.models import BaseModel

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
        return str(self.percent)
