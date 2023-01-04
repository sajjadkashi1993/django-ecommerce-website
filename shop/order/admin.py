from django.contrib import admin
from .models import Order, OrderItem, Transaction
# Register your models here.
class TransactionInline(admin.StackedInline):
    model = Transaction
    extra = 1
class OrderItemInline(admin.TabularInline):
    model = OrderItem

@admin.register(Order)
class OrederAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'grand', 'receiver_mobile','created_at')
    list_filter = ('status',)
    inlines = (OrderItemInline, TransactionInline)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    # raw_id_fields = ('coupon',)

@admin.register(OrderItem)
class OrederItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'warehouse_code', 'price', 'quantity','created_at')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_filter = ('product','order')
