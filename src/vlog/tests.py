from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from vlog import models
from vlog import forms
from vlog import views
from core.views import BaseView
from django.urls import reverse


class TransliterationTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
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


class TestVlog(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='user', password='qwerty123'
        )
        category = models.Category.objects.create(
            title='спорт',
            slug='sport',
            author=self.user
        )
        article = models.Article.objects.create(
            title='футбол',
            slug='football',
            author=self.user,
            category=category
        )
        tag = models.Tag.objects.create(
            title='мяч',
            slug='ball'
        )
        comment = models.Comment.objects.create(
            author=self.user,
            article=article,
            text="ololo"
        )

        article.tags.add(tag)
        article.comments.add(comment)

        BaseView(template_name='ololo.html')
        views.Category.objects.create(
            title='абра-кадабра',
            slug='abra-kadabra',
            author=self.user
        )
        views.Article.objects.create(
            title='тестовая статься',
            slug='testovaya-statia',
            author=self.user,
            category=category
        )


class CategoryModelTestCase(TestVlog):

    def test_category_model_simple_load(self):
        instance = models.Category.objects.create()
        self.assertIsInstance(instance, models.Category)

    def test_category_model(self):
        category = models.Category.objects.get(title='спорт')
        self.assertEqual(category.title, 'спорт')
        self.assertEqual(category.slug, 'sport')
        self.assertEqual(category.author, self.user)

    def test_category_name(self):
        category = models.Category.objects.get(title='спорт')
        expected_name = 'спорт'
        self.assertEqual(str(category), expected_name)


class ArticleModelTestCase(TestVlog):

    def test_article_model_simple_load(self):
        instance = models.Article.objects.create()
        self.assertIsInstance(instance, models.Article)

    def test_article_model(self):
        article = models.Article.objects.get(title='футбол')
        self.assertEqual(article.title, 'футбол')
        self.assertEqual(article.slug, 'football')
        self.assertEqual(article.author, self.user)
        self.assertEqual(article.category.title, 'спорт')

    def test_article_name(self):
        article = models.Article.objects.get(title='футбол')
        expected_name = 'футбол'
        self.assertEqual(str(article), expected_name)

    def test_get_all_method(self):
        self.assertEqual(tuple(models.Article.objects.all()), tuple(models.Article.get_all()))


class TagModelTestCase(TestVlog):

    def test_tag_model_simple_load(self):
        instance = models.Tag.objects.create()
        self.assertIsInstance(instance, models.Tag)

    def test_tag_model(self):
        tag = models.Tag.objects.get(title='мяч')
        self.assertEqual(tag.title, 'мяч')
        self.assertEqual(tag.slug, 'ball')

    def test_tag_name(self):
        tag = models.Tag.objects.get(title='мяч')
        expected_name = 'мяч'
        self.assertEqual(str(tag), expected_name)

    def test_get_all_method(self):
        self.assertEqual(tuple(models.Tag.objects.all()), tuple(models.Tag.get_all()))


class CommentModelTestCase(TestVlog):

    def test_comment_model_simple_load(self):
        instance = models.Comment.objects.create()
        self.assertIsInstance(instance, models.Comment)

    def test_comment_model(self):
        comment = models.Comment.objects.get(author=self.user)
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.article.title, 'футбол')
        self.assertEqual(comment.text, 'ololo')

    def test_comment_name(self):
        comment = models.Comment.objects.get(author=self.user)
        self_author_username = self.user
        self_article_title = 'футбол'
        self.assertEqual(str(comment), f'{self_author_username} [{self_article_title}]')


class BaseViewTestCase(TestVlog):

    @override_settings(DEBUG=True)
    def test_view_url_by_name(self):
        response = self.client.login(
            username='user',
            password='qwerty123'
        )
        self.assertTrue(response)

        response = self.client.get(reverse('vlog:index'))

        self.assertEquals(response.status_code, 200)

        context = response.context

        self.assertTrue('articles' in context)
        self.assertTrue('most_popular_categories' in context)
        self.assertTrue('most_commented_articles' in context)
        self.assertTrue('most_populated_tags' in context)


class PopularCategoriesViewTestCase(TestVlog):

    @override_settings(DEBUG=True)
    def test_view_url_by_name(self):
        response = self.client.login(
            username='user',
            password='qwerty123'
        )
        self.assertTrue(response)

        response = self.client.get(reverse('vlog:popular_categories'))

        self.assertEquals(response.status_code, 200)

        context = response.context

        self.assertTrue('articles' in context)
        self.assertTrue('most_popular_categories' in context)
        self.assertTrue('most_commented_articles' in context)
        self.assertTrue('most_populated_tags' in context)
        self.assertTrue('crumbs' in context)
        self.assertTrue('popular_categories' in context)


class PopulatedTagsViewTestCase(TestVlog):

    @override_settings(DEBUG=True)
    def test_view_url_by_name(self):
        response = self.client.login(
            username='user',
            password='qwerty123'
        )
        self.assertTrue(response)

        response = self.client.get(reverse('vlog:popular_categories'))

        self.assertEquals(response.status_code, 200)

        context = response.context

        self.assertTrue('articles' in context)
        self.assertTrue('most_popular_categories' in context)
        self.assertTrue('most_commented_articles' in context)
        self.assertTrue('most_populated_tags' in context)
        self.assertTrue('crumbs' in context)
        self.assertTrue('popular_categories' in context)


class PopularArticlesViewTestCase(TestVlog):

    @override_settings(DEBUG=True)
    def test_view_url_by_name(self):
        response = self.client.login(
            username='user',
            password='qwerty123'
        )
        self.assertTrue(response)

        response = self.client.get(reverse('vlog:popular_articles'))

        self.assertEquals(response.status_code, 200)

        context = response.context

        self.assertTrue('articles' in context)
        self.assertTrue('most_popular_categories' in context)
        self.assertTrue('most_commented_articles' in context)
        self.assertTrue('most_populated_tags' in context)
        self.assertTrue('crumbs' in context)
        self.assertTrue('popular_articles' in context)


class ArticlesViewTestCase(TestVlog):

    @override_settings(DEBUG=True)
    def test_view_url_by_name(self):
        response = self.client.login(
            username='user',
            password='qwerty123'
        )
        self.assertTrue(response)

        response = self.client.get(reverse('vlog:articles'))

        self.assertEquals(response.status_code, 200)

        context = response.context

        self.assertTrue('articles' in context)
        self.assertTrue('most_popular_categories' in context)
        self.assertTrue('most_commented_articles' in context)
        self.assertTrue('most_populated_tags' in context)
        self.assertTrue('crumbs' in context)
        self.assertTrue('articles' in context)


class CategoriesViewTestCase(TestVlog):

    @override_settings(DEBUG=True)
    def test_view_url_by_name(self):
        response = self.client.login(
            username='user',
            password='qwerty123'
        )
        self.assertTrue(response)

        response = self.client.get(reverse('vlog:categories'))

        self.assertEquals(response.status_code, 200)

        context = response.context

        self.assertTrue('articles' in context)
        self.assertTrue('most_popular_categories' in context)
        self.assertTrue('most_commented_articles' in context)
        self.assertTrue('most_populated_tags' in context)
        self.assertTrue('crumbs' in context)
        self.assertTrue('categories' in context)
        self.assertTrue('paginator' in context)


class ArticleViewTestCase(TestVlog):

    def test_simple_load(self):
        instance = views.Article.objects.get(title='футбол')
        self.assertIsInstance(instance, views.Article)

    def test_article_view(self):
        article = views.Article.objects.get(title='тестовая статься')

        self.assertEqual(article.title, 'тестовая статься')
        self.assertEqual(article.slug, 'testovaya-statia')
        self.assertEqual(article.author, self.user)

    @override_settings(DEBUG=True)
    def test_view_url_by_name(self):
        response = self.client.login(
            username='user',
            password='qwerty123'
        )
        self.assertTrue(response)

        article = models.Article.objects.get(title='футбол')
        response = self.client.get(
            reverse('vlog:article', args=[article.category.slug, article.slug])
        )

        self.assertEquals(response.status_code, 200)

        context = response.context

        self.assertTrue('articles' in context)
        self.assertTrue('most_popular_categories' in context)
        self.assertTrue('most_commented_articles' in context)
        self.assertTrue('most_populated_tags' in context)
        self.assertTrue('crumbs' in context)
        self.assertTrue('article' in context)
        self.assertTrue('category' in context)


class CategoryViewTestCase(TestVlog):

    def test_category_simple_load(self):
        instance = views.Category.objects.get(title='спорт')
        self.assertIsInstance(instance, views.Category)

    def test_category_view(self):
        category = views.Category.objects.get(title='абра-кадабра')

        self.assertEqual(category.title, 'абра-кадабра')
        self.assertEqual(category.slug, 'abra-kadabra')
        self.assertEqual(category.author, self.user)

    @override_settings(DEBUG=True)
    def test_view_url_by_name(self):
        response = self.client.login(
            username='user',
            password='qwerty123'
        )
        self.assertTrue(response)

        article = views.Article.objects.get(title='футбол')

        response = self.client.get(reverse('vlog:category', args=[article.category.slug]))

        self.assertEquals(response.status_code, 200)

        context = response.context

        self.assertTrue('articles' in context)
        self.assertTrue('most_popular_categories' in context)
        self.assertTrue('most_commented_articles' in context)
        self.assertTrue('most_populated_tags' in context)
        self.assertTrue('crumbs' in context)
        self.assertTrue('category' in context)
        self.assertTrue('articles' in context)


class TagsViewTestCase(TestVlog):

    @override_settings(DEBUG=True)
    def test_view_url_by_name(self):
        response = self.client.login(
            username='user',
            password='qwerty123'
        )
        self.assertTrue(response)

        response = self.client.get(reverse('vlog:tags'))

        self.assertEquals(response.status_code, 200)

        context = response.context

        self.assertTrue('articles' in context)
        self.assertTrue('most_popular_categories' in context)
        self.assertTrue('most_commented_articles' in context)
        self.assertTrue('most_populated_tags' in context)
        self.assertTrue('crumbs' in context)
        self.assertTrue('tags' in context)


class TagViewTestCase(TestVlog):

    @override_settings(DEBUG=True)
    def test_view_url_by_name(self):
        response = self.client.login(
            username='user',
            password='qwerty123'
        )
        self.assertTrue(response)

        tag = models.Tag.objects.get(title='мяч')
        response = self.client.get(reverse('vlog:tag', args=[tag.slug]))

        self.assertEquals(response.status_code, 200)

        context = response.context

        self.assertTrue('articles' in context)
        self.assertTrue('most_popular_categories' in context)
        self.assertTrue('most_commented_articles' in context)
        self.assertTrue('most_populated_tags' in context)
        self.assertTrue('crumbs' in context)
        self.assertTrue('articles' in context)
        self.assertTrue('tag' in context)
