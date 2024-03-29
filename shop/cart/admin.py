from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.


class CartItemline(admin.TabularInline):
    model = CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'updated_at')
    inlines = (CartItemline,)
    # def has_add_permission(self, request):
    #     return False


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'product', 'updated_at')

    def has_add_permission(self, request):
        return False
