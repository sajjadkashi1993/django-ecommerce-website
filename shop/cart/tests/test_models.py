from django.test import TestCase
from ..models import Cart, CartItem
from model_bakery import baker


class CartTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        baker.make(Cart, user__phone ='09128812994')

    def setUp(self) -> None:
        self.cart = Cart.objects.get(id=1)

    def test_str(self):
        self.assertEqual(str(self.cart), '09128812994: 2')


class CartItemTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cart_item = baker.make(CartItem)

    def setUp(self) -> None:
        self.cart_item = CartItem.objects.get(id=1)

    def test_str(self):
        self.assertEqual(str(self.cart_item), '1')