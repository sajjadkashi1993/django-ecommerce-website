from datetime import timedelta
from django.test import TestCase
from django.utils.timezone import now

from model_bakery import baker
from ..models import Product, Price, Gallery, Image, Category, Property
from discount.models import Discount

class CategoryTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make(Category, title='title title', slug='title-title')
    def setUp(self) -> None:
        self.category = Category.objects.get(id=1)

    def test_str(self):
        self.assertEqual(str(self.category), 'title')

    def test_get_absolute_url(self):
        url = self.category.get_absolute_url()
        self.assertEqual(url, 'ttle')


class ProductTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        d = baker.make(Discount,type=1,percent=25, start_time=now(), expire_time=now()+timedelta(days=7))
        p = baker.make(Product, discount=d, title='title')
        gallery = baker.make(Gallery, product=p, main_pic='ddd')
        baker.make(Price,product=p, amount=10)
        baker.make(Price,product=p, amount=20)
    def setUp(self) -> None:
        self.product = Product.objects.get(id=1)

    def test_str(self):
        self.assertEqual(str(self.product), 'title')

    def test_user_label(self):
        user_label = Product._meta.get_field('user').verbose_name
        self.assertEqual(user_label, 'user')

    def test_get_url_main_image(self):
        url =self.product.get_url_main_image()
        self.assertEqual(url, '/media/ddd')

    def test_get_last_price(self):
        price =self.product.get_last_price()
        self.assertEqual(price, 20.00)

    def test_get_after_discount_price(self):
        price = self.product.get_after_discount_price()
        self.assertEqual(price, 15.00)

    def test_is_new(self):
        new = self.product.is_new()
        self.assertEqual(new, True)





class PriceTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make(Price, amount=12)

    def setUp(self) -> None:
        self.price = Price.objects.get(id=1)

    def test_str(self):
        self.assertEqual(str(self.price).split(':')[-1], '12.00')


class CategoryTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make(Category, title='title')

    def setUp(self) -> None:
        self.category = Category.objects.get(id=1)

    def test_str(self):
        self.assertEqual(str(self.category), 'title')

class ImageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make(Image, name='name')

    def setUp(self) -> None:
        self.image = Image.objects.get(id=1)

    def test_str(self):
        self.assertEqual(str(self.image), 'name')


class GalleryTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make(Gallery, name='name')

    def setUp(self) -> None:
        self.gallery = Gallery.objects.get(id=1)

    def test_str(self):
        self.assertEqual(str(self.gallery), '1')

class PropertyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make(Property, key='key', value='value')

    def setUp(self) -> None:
        self.property = Property.objects.get(id=1)

    def test_str(self):
        self.assertEqual(str(self.property), 'key:value')