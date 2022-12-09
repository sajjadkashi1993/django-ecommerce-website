from django.db import models
from core.models import BaseModel

# Create your models here.


class Coupon(BaseModel):
    code = models.CharField(max_length=10)
    min_purchase = models.DecimalField(max_digits=20, decimal_places=2)
    max_discount = models.DecimalField(max_digits=20, decimal_places=2)
    percent = models.PositiveSmallIntegerField()
    expire_time = models.DateTimeField()
    limit_number = models.IntegerField()
    start_time = models.DateTimeField()
    event = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.code


class Discount(BaseModel):
    class TYPE(models.IntegerChoices):
        percent = 1, 'Percent'
        amount = 2, 'Amount'

    type = models.IntegerField(choices=TYPE.choices)
    percent = models.PositiveSmallIntegerField(null=True, blank=True)
    amount = models.DecimalField(
        max_digits=20, decimal_places=2, null=True, blank=True)

    start_time = models.DateTimeField()
    expire_time = models.DateTimeField()
    event = models.CharField(max_length=100)


    def __str__(self) -> str:
        return str(self.percent)
