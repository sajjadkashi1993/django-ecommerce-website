from django.test import TestCase
from ..models import Discount, Coupon
from model_bakery import baker


class CouponTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make(Coupon, code='1234')

    def setUp(self) -> None:
        self.coupon = Coupon.objects.get(id=1)

    def test_str(self):
        self.assertEqual(str(self.coupon), '1234')


class DiscountTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make(Discount, type=1, percent=10)
        baker.make(Discount, type=2, amount=10)

    def setUp(self) -> None:
        self.discount_percent = Discount.objects.get(id=1)
        self.discount_amount = Discount.objects.get(id=2)

    def test_str(self):
        self.assertEqual(str(self.discount_percent), '10%')
        self.assertEqual(str(self.discount_amount), '10.00$')
