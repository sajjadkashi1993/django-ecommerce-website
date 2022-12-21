from django.test import TestCase
from model_bakery import baker
from ..sms import APIException,HTTPException,SmsAPI

class APIExceptionTests(TestCase):

    def test_is_exception(self):
        self.assertIsInstance(APIException(), Exception)


class HTTPExceptionTests(TestCase):

    def test_is_exception(self):
        self.assertIsInstance(HTTPException(), Exception)


class SmsApiTests(TestCase):

    def setUp(self) -> None:
        self.sms = SmsAPI(apikey='1111')

    def test_str(self):
        self.assertEqual(str(self.sms), 'sms.SmsAPI(1111)')

    def test_reper(self):
        self.assertEqual(repr(self.sms), "sms.SmsAPI('1111')")