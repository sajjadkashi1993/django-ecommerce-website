from datetime import timedelta
from decimal import Decimal
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from core.models import BaseModel, SoftDeleteModel
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils.html import mark_safe

from discount.models import Discount

User = get_user_model()
max_digits = settings.MAX_DIGITS
decimal_places = settings.DECIMAL_PLACES


class Category(BaseModel):
    """
        Id:	The unique id to identify the category.
        Parent:	The parent id to identify the parent category.
        Title: The category title.
        Slug: The category slug to form the URL.
        Content: The column used to store the category details.
        Image: The picture for the category
    """
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, verbose_name=_('parent'), null=True, blank=True, related_name='childrens')
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'), unique=True)
    content = models.TextField(_('content'), null=True, blank=True)
    image = models.ImageField(
        _('image'), upload_to='category/', null=True, blank=True)
    is_navbar = models.BooleanField(_('is_navbar'))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _('Categories')

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("product:cat", kwargs={"slug": self.slug})

    def get_children(self):
        children = list()
        children.append(self)
        for child in self.childrens.all():
            children.extend(child.get_children())
        return children


class Product(SoftDeleteModel):
    """
        Id:	The unique id to identify the product.
        User: The user id to identify the admin or vendor.
        Title:	The product title to be displayed on the Shop Page and Product Page.
        Slug:	The slug to form the URL.
        Warehouse Code:	The warehouse code to track the product inventory.
        Discount:	The discount on the product.
        Quantity:	The available quantity of the product.
        Is Shop:	It can be used to identify whether the product is publicly available for shopping.
        Created At:	It stores the date and time at which the product is created.
        Updated At:	It stores the date and time at which the product is updated.
        Published At:	It stores the date and time at which the product is published on the Shop.
        Starts At:	It stores the date and time at which the product sale starts.
        Ends At:	It stores the date and time at which the product sale ends.
        Content:	The column used to store the additional details of the product.
    """
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name=_(
        'category'), related_name='products')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('user'),
                             related_name='products')
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'), unique=True)
    is_shop = models.BooleanField(_('is shop'), default=False)
    warehouse_code = models.CharField(_('warehouse code'), max_length=50)
    discount = models.ForeignKey(
        Discount, on_delete=models.SET_NULL, verbose_name=_('discount'), null=True, blank=True)
    quantity = models.PositiveIntegerField(_('quantity'),)
    published_at = models.DateTimeField(
        _('published at'), null=True, blank=True)
    starts_at = models.DateTimeField(_('starts at'), null=True, blank=True)
    ends_at = models.DateTimeField(_('ends at'), null=True, blank=True)

    content = models.TextField(_('content'),)
    brand = models.CharField(_('brand'), max_length=100)

    class Meta:
        verbose_name = _("Products")
        verbose_name_plural = _('Products')

    def __str__(self) -> str:
        return self.title

    def get_url_main_image(self):
        galery = self.galery
        url = galery.main_pic.url
        return url

    def get_absolute_url(self):
        # return reverse("model_detail", kwargs={"pk": self.pk})
        pass

    def get_last_price(self):
        price = self.prices.first()
        print(price)
        return price.amount

    def get_after_discount_price(self):
        if self.discount and self.discount.expire_time > now() and self.discount.start_time <= now():
            if self.discount.type == 1:
                price = self.get_last_price() * Decimal(1 - (self.discount.percent/100))
                return round(price, 2)
            elif self.discount.type == 2:
                price = self.get_last_price() - self.discount.amount
                if price > 0:
                    return price
                else:
                    return 0
        return self.get_last_price()

    def is_new(self):
        if now() - self.created_at < timedelta(days=7):
            return True
        return False


class Price(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_('product'),  related_name='prices')
    amount = models.DecimalField(
        _('amount'), max_digits=max_digits, decimal_places=decimal_places)

    class Meta:
        verbose_name = _("price")
        verbose_name_plural = _('prices')
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'{self.created_at}:{self.amount}'


class Gallery(BaseModel):
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, verbose_name=_('product'),  related_name='galery')
    main_pic = models.ImageField(_('main pic'), upload_to='category/')
    name = models.CharField(_('name'), max_length=50)
    
    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _('Galleries')

    def __str__(self) -> str:
        return str(self.id)


class Image(BaseModel):
    gallery = models.ForeignKey(
        Gallery, on_delete=models.CASCADE, verbose_name=_('gallery'),  related_name='images')
    image_alt = models.CharField(_('image alt'), max_length=50)
    image = models.ImageField(_('image'), upload_to='image/')
    name = models.CharField(_('name'), max_length=50)

    class Meta:
        verbose_name = _("image")
        verbose_name_plural = _('images')

    def __str__(self) -> str:
        return self.name

    def image_tag(self):
            return mark_safe('<img src="%s" width="100" height="100" />' % (self.image.url))

    image_tag.short_description = 'Image'

class Property(BaseModel):
    """ 
        This model stores the attributes of the product as key: value

        Product: The product id to identify the parent product.
        Key: The key identifying the meta.
        Value: The column used to store the product metadata.
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_('product'),  related_name='property')
    key = models.CharField(_('key'), max_length=50)
    value = models.CharField(_('value'), max_length=50)

    class Meta:
        verbose_name = _("Property")
        verbose_name_plural = _('Properties')

    def __str__(self) -> str:
        return f'{self.key}:{self.value}'
