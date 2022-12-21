from django.test import TestCase, Client
from django.urls import reverse
from model_bakery import baker
from ..forms import CommentForm

class TestCreateCommentView(TestCase):

    def setUp(self) -> None:
        self.client = Client()

    def test_create_comment_post_valid(self):
        response = self.client.post(reverse('comment:create_comment', kwargs={'pk':1}))
        self.assertEqual(response.status_code, 200)