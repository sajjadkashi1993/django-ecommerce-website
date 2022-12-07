from django.contrib import admin
from .models import Discount, Coupon
# Register your models here.




@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    pass