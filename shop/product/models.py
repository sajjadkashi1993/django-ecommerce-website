from django.db import models
from core.models import BaseModel
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from discount.models import Discount
User = get_user_model()


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
        'Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='childrens')
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='category/', null=True, blank=True)
    is_navbar = models.BooleanField()

    def __str__(self) -> str:
        return self.title


class Product(BaseModel):
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
    category = models.ForeignKey(Category,on_delete=models.PROTECT, related_name='product')
    user = models.ForeignKey(User, on_delete=models.PROTECT,
                             related_name='products', verbose_name=_('User'),)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    is_shop = models.BooleanField(default=False)
    warehouse_code = models.CharField(max_length=50)
    discount = models.ForeignKey(
        Discount, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    published_at = models.DateTimeField(null=True, blank=True)
    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)

    content = models.TextField()
    brand = models.CharField(max_length=100)

    is_delete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class Price(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name='prices')
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.created_at}:{self.amount}'


class Gallery(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name='galery')
    main_pic = models.ImageField(upload_to='category/')
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Image(BaseModel):
    galery = models.ForeignKey(
        Gallery, on_delete=models.CASCADE, related_name='images')
    image_alt = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/')
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Property(BaseModel):
    """ 
        This model stores the attributes of the product as key: value

        Product: The product id to identify the parent product.
        Key: The key identifying the meta.
        Value: The column used to store the product metadata.
    """

    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name='property')
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.key}:{self.value}'
