from django.contrib.auth import get_user_model
from django.forms import ValidationError
from django.test import TestCase
from ..models import Address, ProfileUser, OtpCode, User


class UsersManagersTests(TestCase):


    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(phone='09128812994')
        self.assertEqual(user.phone, '09128812994')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(password="foo")
        with self.assertRaises(ValueError):
            User.objects.create_user(phone='')
        # with self.assertRaises(ValidationError):
        #     User.objects.create_user(phone='4444')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            phone='09128812994', password='foo')
        self.assertEqual(admin_user.phone, '09128812994')

        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                phone='09128812994', password='foo', is_superuser=False)

    def test_str(self):
        User = get_user_model()
        user = User.objects.create_user(phone='09128812994')
        self.assertEqual(str(user),'09128812994')

class AddressTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(phone='09128812990')

    def setUp(self) -> None:
        self.user=User.objects.get(id=1)
        self.a= Address.objects.create(profile=self.user.profile,
                               country='country',
                               province='province',
                               city='city',
                               adderess='adderess',
                               postal_code='postal_code',)
        return super().setUp()

    def test_creation_address(self):
        
        self.assertEqual(self.a.profile,self.user.profile)
        self.assertEqual(self.a.country,'country')
        self.assertEqual(self.a.province,'province')
        self.assertEqual(self.a.city,'city')
        self.assertEqual(self.a.adderess,'adderess')
        self.assertEqual(self.a.postal_code,'postal_code')

    def test_str(self):
        self.assertEqual(str(self.a),'country, province, city, adderess')

class OtpCodeTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        OtpCode.objects.create(phone='09128812994',code='12345')

    def setUp(self):
        self.o=OtpCode.objects.get(id=1)

    def test_creation_otp_cod(self):
        self.assertEqual(self.o.phone,'09128812994')
        self.assertEqual(self.o.code,'12345')
        self.assertEqual(self.o.number_try,0)

    def test_phone_label(self):
        phone_label = OtpCode._meta.get_field('phone').verbose_name
        self.assertEqual(phone_label, 'phone number')

    def test_phone_max_length(self):
        max_length = self.o._meta.get_field('phone').max_length
        self.assertEqual(max_length, 11)

    def test_str(self):
        self.assertEqual(str(self.o),'12345')