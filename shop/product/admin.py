from django.contrib import admin
from .models import Category, Product, Gallery, Image, Price, Property
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_navbar', 'parent')
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('is_navbar', 'parent')
    raw_id_fields = ('parent',)
    search_fields = ('title',)


class GalleryInline(admin.StackedInline):
    model = Gallery


class PriceInline(admin.TabularInline):
    model = Price


class PropertyInline(admin.TabularInline):
    model = Property


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (GalleryInline, PriceInline, PropertyInline)
    list_display = ('id', 'title', 'category',  'is_shop', 'discount', 'quantity')
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('discount', 'category')
    raw_id_fields = ('discount',)
    # autocomplete_fields = ('category',)
    search_fields = ('title', 'category')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'gallery', 'image_alt', 'image', 'image_tag')
    raw_id_fields = ('gallery', )
    list_editable = ('image',)
    readonly_fields = ('image_tag',)
