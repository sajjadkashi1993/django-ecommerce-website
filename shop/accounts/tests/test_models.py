from django.contrib.auth import get_user_model
from django.forms import ValidationError
from django.test import TestCase
from .models import Address, ProfileUser, OtpCode, User


# class UsersManagersTests(TestCase):

#     def test_create_user(self):
#         User = get_user_model()
#         user = User.objects.create_user(phone='09128812994')
#         self.assertEqual(user.phone, '09128812994')
#         self.assertTrue(user.is_active)
#         self.assertFalse(user.is_staff)
#         self.assertFalse(user.is_superuser)
#         try:
#             # username is None for the AbstractUser option
#             # username does not exist for the AbstractBaseUser option
#             self.assertIsNone(user.username)
#         except AttributeError:
#             pass
#         with self.assertRaises(TypeError):
#             User.objects.create_user()
#         with self.assertRaises(TypeError):
#             User.objects.create_user(password="foo")
#         # with self.assertRaises(ValidationError):
#         #     User.objects.create_user(phone='4')

#     def test_create_superuser(self):
#         User = get_user_model()
#         admin_user = User.objects.create_superuser(
#             phone='09128812994', password='foo')
#         self.assertEqual(admin_user.phone, '09128812994')

#         self.assertTrue(admin_user.is_active)
#         self.assertTrue(admin_user.is_staff)
#         self.assertTrue(admin_user.is_superuser)
#         try:
#             # username is None for the AbstractUser option
#             # username does not exist for the AbstractBaseUser option
#             self.assertIsNone(admin_user.username)
#         except AttributeError:
#             pass
#         with self.assertRaises(ValueError):
#             User.objects.create_superuser(
#                 phone='09128812994', password='foo', is_superuser=False)


class AddressTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone='09128812990')
        self.profile = ProfileUser(user=self.user)
        self.profile.save()
    def test_creation_Contact(self):
        a= Address.objects.create(profile=self.profile,
                               country='country',
                               province='province',
                               city='city',
                               adderess='adderess',
                               postal_code='postal_code',)
        self.assertEqual(a.profile,self.profile)
        self.assertEqual(a.country,'country')
        self.assertEqual(a.province,'province')
        self.assertEqual(a.city,'city')
        self.assertEqual(a.adderess,'adderess')
        self.assertEqual(a.postal_code,'postal_code')