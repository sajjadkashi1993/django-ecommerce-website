from django.test import TestCase, Client
from django.urls import reverse
from model_bakery import baker
from ..forms import UserLoginRegisterForm
from ..models import OtpCode


class TestLoginRegisteruser(TestCase):

    def setUp(self) -> None:
        self.client = Client()

    def test_login_register_get(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.failUnless(response.context['form'], UserLoginRegisterForm)

    def test_login_register_post_valid(self):
        response = self.client.post(reverse('accounts:login'), data={
                                    'phone': '09128812994'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accounts:verify'))
        self.assertEqual(OtpCode.objects.count(), 1)
        # self.assertEqual(response.session['user_login_info'],'1')
        # self.mes()
