from django.contrib import admin
from .models import Category, Product, Gallery, Image, Price, Property
# Register your models here.

admin.site.register([Category, Image])


class GalleryInline(admin.TabularInline):
    model = Gallery


class PriceInline(admin.TabularInline):
    model = Price


class PropertyInline(admin.TabularInline):
    model = Property


@admin.register(Product)
class CustomUserAdmin(admin.ModelAdmin):
    inlines = (GalleryInline, PriceInline, PropertyInline)
