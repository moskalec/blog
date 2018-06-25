from django.contrib.auth import get_user_model
from django.test import TestCase
from vlog import models
from vlog import forms
from vlog import views
from core.views import BaseView


class TransliterationTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='user', password='qwerty123'
        )

    def test_transliteration(self):
        cat_form = forms.CategoryForm(
            {'title': 'спорт', 'author': self.user.pk}
        )

        cat = None

        if cat_form.is_valid():
            cat = cat_form.save()

        self.assertEqual(cat.slug, 'sport')

        cat_form = forms.CategoryForm(
            {'title': 'тест'}, instance=cat
        )

        if cat_form.is_valid():
            cat = cat_form.save()

        self.assertEqual(cat.slug, 'test')

        cat_form = forms.CategoryForm(
            {'title': 'Breaking News! Новости.'}, instance=cat
        )

        if cat_form.is_valid():
            cat = cat_form.save()

        self.assertEqual(cat.slug, 'breaking-news-novosti')


class BaseViewTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='user', password='qwerty123'
        )
        BaseView(template_name = 'ololo.html')

    def test_base_view_simple_load(self):
        instance = BaseView()
        self.assertIsInstance(instance, BaseView)

    def test_base_view_template(self):
        self.assertEqual(BaseView.template_name, '')


class CategoryViewTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='user', password='qwerty123'
        )
        views.Category.objects.create(
            title='абра-кадабра',
            slug='abra-kadabra',
            author=self.user
        )

    def test_category_simple_load(self):
        instance = models.Category.objects.get()
        self.assertIsInstance(instance, views.Category)

    def test_category_view(self):
        category = views.Category.objects.get(title='абра-кадабра')

        self.assertEqual(category.title, 'абра-кадабра')
        self.assertEqual(category.slug, 'abra-kadabra')
        self.assertEqual(category.author, self.user)


class ArticleViewTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='user', password='qwerty123'
        )
        views.Article.objects.create(
            title='тестовая статься',
            slug='testovaya-statia',
            author=self.user
        )

    def test_simple_load(self):
        instance = views.Article.objects.get()
        self.assertIsInstance(instance, views.Article)

    def test_article_view(self):
        article = views.Article.objects.get(title='тестовая статься')

        self.assertEqual(article.title, 'тестовая статься')
        self.assertEqual(article.slug, 'testovaya-statia')
        self.assertEqual(article.author, self.user)
