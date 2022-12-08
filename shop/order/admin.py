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
    inlines = (OrderItemInline, TransactionInline)


@admin.register(OrderItem)
class OrederAdmin(admin.ModelAdmin):
    pass