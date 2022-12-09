from django.test import TestCase
from ..models import Order, OrderItem, Transaction
from model_bakery import baker


class OrderTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make(Order, user__phone='09128812994')

    def setUp(self) -> None:
        self.order = Order.objects.get(id=1)

    def test_str(self):
        self.assertEqual(str(self.order), '09128812994, 1')


class OrderItemTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make(OrderItem, quantity=3, product__title='aaaa')

    def setUp(self) -> None:
        self.order_item = OrderItem.objects.get(id=1)

    def test_str(self):
        self.assertEqual(str(self.order_item), 'aaaa:3')


class TransactionTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make(Transaction, order__user__phone='09128812994', code='1234')

    def setUp(self) -> None:
        self.transaction = Transaction.objects.get(id=1)

    def test_str(self):
        self.assertEqual(str(self.transaction), '09128812994, 1:1234')
