from datetime import timedelta
from django.test import TestCase
from django.utils.timezone import now

from model_bakery import baker
from ..models import Product, Price, Gallery, Image, Category, Property
from discount.models import Discount
from comment.models import Comment


class CategoryTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make(Category, title='title', slug='title-title')
    def setUp(self) -> None:
        self.category = Category.objects.get(id=1)

    def test_str(self):
        self.assertEqual(str(self.category), 'title')

    def test_get_absolute_url(self):
        url = self.category.get_absolute_url()
        self.assertEqual(url, '/product/shop/title-title')

    def test_get_children(self):
        cat2 = baker.make(Category, parent=self.category)
        cat3 = baker.make(Category, parent=cat2)
        categories = self.category.get_children()
        self.assertEqual(categories, [self.category,cat2, cat3])



class ProductTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        d = baker.make(Discount,type=1,percent=25, start_time=now(), expire_time=now()+timedelta(days=7))
        p = baker.make(Product, discount=d, title='title')

        gallery = baker.make(Gallery, product=p, main_pic='ddd')
        baker.make(Price,product=p, amount=10)
        baker.make(Price,product=p, amount=20)
        cm1 = baker.make(Comment,rate=2, product=p, status=2)
        cm2 = baker.make(Comment,rate=4, product=p, status=2)
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

    def test_get_absolute_url(self):
        url =self.product.get_absolute_url()
        self.assertEqual(url, '/product/1/')

    def test_get_last_price(self):
        price =self.product.get_last_price()
        self.assertEqual(price, 20.00)

    def test_get_after_discount_price(self):
        price = self.product.get_after_discount_price()
        self.assertEqual(price, 15.00)

    def test_is_new(self):
        new = self.product.is_new()
        self.assertEqual(new, True)

    def test_average_rating(self):
        avg = self.product.average_rating()
        self.assertEqual(avg, 3)




class PriceTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make(Price, amount=12)

    def setUp(self) -> None:
        self.price = Price.objects.get(id=1)

    def test_str(self):
        self.assertEqual(str(self.price).split(':')[-1], '12.00')


class ImageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make(Image, name='name', image='1')
        

    def setUp(self) -> None:
        self.image = Image.objects.get(id=1)

    def test_str(self):
        self.assertEqual(str(self.image), 'name')
    
    def test_image_tag(self):
        image_tag = self.image.image_tag()
        self.assertEqual(image_tag, '<img src="/media/1" width="100" height="100" />')


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