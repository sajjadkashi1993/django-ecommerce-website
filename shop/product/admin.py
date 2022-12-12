from django.contrib import admin
from .models import Category, Product, Gallery, Image, Price, Property
# Register your models here.

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('gallery', 'image_alt', 'name')
    raw_id_fields = ('gallery', )
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ('title', 'slug', 'is_navbar', 'parent')
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('is_navbar','parent')
    raw_id_fields = ('parent',)

class GalleryInline(admin.TabularInline):
    model = Gallery


class PriceInline(admin.TabularInline):
    model = Price


class PropertyInline(admin.TabularInline):
    model = Property


@admin.register(Product)
class CustomUserAdmin(admin.ModelAdmin):
    inlines = (GalleryInline, PriceInline, PropertyInline)
    list_display = ('title','category',  'is_shop', 'discount', 'quantity')
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('discount','category')
    raw_id_fields =('discount',)


