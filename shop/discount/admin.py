from django.contrib import admin
from .models import Discount, Coupon
# Register your models here.


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('type', 'percent', 'amount',
                    'start_time', 'expire_time', 'event')
    list_filter = ('event', 'type')
    date_hierarchy = 'start_time'
    ordering = ('-start_time', '-expire_time')


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'percent', 'expire_time', 'start_time', 'event')
    # list_editable = ('expire_time', 'start_time')
    list_filter = ('event',)
    date_hierarchy = 'start_time'
    ordering = ('-start_time', '-expire_time')
