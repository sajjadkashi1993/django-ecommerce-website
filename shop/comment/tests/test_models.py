from django.test import TestCase
from ..models import Comment
from model_bakery import baker


class CommentTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make(Comment, body='body')

    def setUp(self) -> None:
        self.comment = Comment.objects.get(id=1)

    def test_str(self):
        self.assertEqual(str(self.comment), 'body')
