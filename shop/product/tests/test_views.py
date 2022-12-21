from django.test import TestCase, Client
from django.urls import reverse
from model_bakery import baker
from discount.models import Discount
from comment.models import Comment

from ..models import Product, Price, Category


class TestProductListView(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.category1 = baker.make(Category, slug='cat1')
        self.category11 = baker.make(
            Category, slug='cat11', parent=self.category1)
        self.category111 = baker.make(
            Category, slug='cat111', parent=self.category11)
        for _ in range(7):
            p = baker.make(Product, category=self.category11)
            baker.make(Price, product=p)
        for _ in range(7):
            p = baker.make(Product, category=self.category111)
            baker.make(Price, product=p)

    def test_product_list_get_category(self):
        response = self.client.get(reverse('product:shop'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/shop.html')
        products = Product.undeleted_objects.all()[0:12]
        self.failIf(list(response.context['products']) != list(products))

    def test_product_list_get_slug(self):
        response = self.client.get(
            reverse('product:cat', kwargs={'slug': 'cat1'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/shop.html')
        products = Product.undeleted_objects.filter(
            category__in=[self.category1, self.category11, self.category111])[0:12]
        self.failIf(list(response.context['products']) != list(products))


class TestProducOfferListView(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.discunt = baker.make(Discount)

        for _ in range(3):
            p = baker.make(Product, discount=self.discunt)
            baker.make(Price, product=p)
        for _ in range(7):
            p = baker.make(Product)
            baker.make(Price, product=p)

    def test_product_list_get_category(self):
        response = self.client.get(reverse('product:offer'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/shop.html')
        products = Product.undeleted_objects.filter(id__in=[1, 2, 3])
        self.failIf(list(response.context['products']) != list(products))


class TestProductSearchListView(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        for _ in range(7):
            p = baker.make(Product)
            baker.make(Price, product=p)

        p = baker.make(Product, title='sajjad')
        baker.make(Price, product=p)

    def test_product_list_get_category(self):
        response = self.client.get(
            reverse('product:search'), QUERY_STRING='search=sajjad')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/shop.html')
        products = Product.undeleted_objects.filter(id=8)
        self.failIf(list(response.context['products']) != list(products))


class TestProductDetailView(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.category = baker.make(Category)

        p1 = baker.make(Product, title='sajjad', category=self.category)
        baker.make(Price, product=p1)

        for _ in range(5):
            p = baker.make(Product, category=self.category)
            baker.make(Price, product=p)

        for _ in range(3):
            baker.make(Comment, status=2, is_reply=False, product=p1)

    def test_product_list_get_category(self):
        response = self.client.get(
            reverse('product:product', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product.html')

        product = Product.undeleted_objects.filter(id=1).first()
        self.failIf(response.context['product'] != product)

        comments = Comment.objects.filter(id__in=[1, 2, 3])
        self.failIf(list(response.context['comments']) != list(comments))

        related_product = Product.undeleted_objects.filter(id__in=[2, 3, 4, 5])
        self.failIf(
            list(response.context['related_product']) != list(related_product))
