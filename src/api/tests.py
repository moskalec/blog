import ujson
from django.shortcuts import reverse

from rest_framework.test import APITestCase
from vlog.models import Category, Article, Tag


class TestNoteApi(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(title="test", slug="test")
        self.category.save()
        self.article = Article.objects.create(title="test", slug='test')
        self.article.save()
        self.tag = Tag.objects.create(title="test", slug="test")
        self.tag.save()

    def test_category_creation(self):
        response = self.client.get(reverse('category-list'))

        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(200, response.status_code)

    def test_article_creation(self):
        response = self.client.get(reverse('article-list'))

        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(200, response.status_code)

    def test_tag_creation(self):
        response = self.client.get(reverse('tag-list'))

        self.assertEqual(Tag.objects.count(), 1)
        self.assertEqual(200, response.status_code)

    def test_getting_categories(self):
        response = self.client.get(reverse('category-list'), format="json")
        data = ujson.loads(response.content)

        self.assertTrue(isinstance(data, dict))
        self.assertEqual(data['results'][0]['title'], 'test')
        self.assertTrue('created' in data['results'][0])
        self.assertTrue('updated' in data['results'][0])

    def test_getting_category_detail(self):
        response = self.client.get(reverse('category-detail', kwargs={'slug': 'test'}), format="json")
        data = ujson.loads(response.content)

        self.assertEqual(response.data['slug'], 'test')
        self.assertTrue(isinstance(data, dict))
        self.assertEqual(data['title'], 'test')
        self.assertEqual(data['slug'], 'test')
        self.assertTrue('created' in data)
        self.assertTrue('updated' in data)

    def test_getting_articles(self):
        response = self.client.get(reverse('article-list'), format="json")
        data = ujson.loads(response.content)

        self.assertTrue(isinstance(data, dict))
        self.assertEqual(data['results'][0]['title'], 'test')
        self.assertTrue('created' in data['results'][0])
        self.assertTrue('updated' in data['results'][0])

    def test_getting_article_detail(self):
        response = self.client.get(reverse('article-detail', kwargs={'slug': 'test'}), format="json")
        data = ujson.loads(response.content)

        self.assertEqual(response.data['slug'], 'test')
        self.assertTrue(isinstance(data, dict))
        self.assertEqual(data['title'], 'test')
        self.assertEqual(data['slug'], 'test')
        self.assertTrue('created' in data)
        self.assertTrue('updated' in data)

    def test_getting_tags(self):
        response = self.client.get(reverse('tag-list'), format="json")
        data = ujson.loads(response.content)

        self.assertTrue(isinstance(data, dict))
        self.assertEqual(data['results'][0]['title'], 'test')
        self.assertTrue('created' in data['results'][0])
        self.assertTrue('updated' in data['results'][0])

    def test_getting_tag_detail(self):
        response = self.client.get(reverse('tag-detail', kwargs={'pk': 1}), format="json")
        data = ujson.loads(response.content)

        self.assertEqual(response.data['slug'], 'test')
        self.assertTrue(isinstance(data, dict))
        self.assertEqual(data['title'], 'test')
        self.assertEqual(data['slug'], 'test')
        self.assertTrue('created' in data)
        self.assertTrue('updated' in data)
