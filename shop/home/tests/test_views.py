from django.test import TestCase, Client
from django.urls import reverse
 
class TestContactUsView(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_contact_get(self):
        response = self.client.get(reverse('home:contact-us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact-us.html')

    def test_contact_post_valid(self):
        response = self.client.post(reverse('home:contact-us'))
        self.assertEqual(response.status_code, 200)




