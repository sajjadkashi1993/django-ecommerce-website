from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.

class CartItemline(admin.TabularInline):
    model = CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = (CartItemline,)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass