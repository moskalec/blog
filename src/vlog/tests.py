from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
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


class TestVlog(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='user', password='qwerty123'
        )
        category = models.Category.objects.create(
            title='спорт',
            slug='sport',
            author=self.user
        )
        self.article = models.Article.objects.create(
            title='футбол',
            slug='football',
            author=self.user,
            category=category
        )
        models.Tag.objects.create(
            title='мяч',
            slug='ball',
            # articles=('football', )
        )
        models.Comment.objects.create(
            author=self.user,
            # article=#####,
            # text="ololo"
        )
        BaseView(template_name = 'ololo.html')
        views.Category.objects.create(
            title='абра-кадабра',
            slug='abra-kadabra',
            author=self.user
        )
        views.Article.objects.create(
            title='тестовая статься',
            slug='testovaya-statia',
            author=self.user
        )

        self.factory = RequestFactory()


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


class CommentModelTestCase(TestVlog):

    def test_comment_model_simple_load(self):
        instance = models.Comment.objects.create()
        self.assertIsInstance(instance, models.Comment)

    def test_comment_model(self):
        comment = models.Comment.objects.get(author = self.user)
        self.assertEqual(comment.author, self.user)
        # self.assertEqual(comment.article, 'ololo')
        # self.assertEqual(comment.text, 'ololo')

    # def test_comment_name(self):
        # comment = models.Comment.objects.get(author = self.user, article = )
        # self_author_username = self.user
        #self_article_title = #####
        # self.assertEqual(str(comment), f'{self_author_username} [{self_article_title}]')


class BaseViewTestCase(TestVlog):

    def test_base_view_simple_load(self):
        instance = BaseView()
        self.assertIsInstance(instance, BaseView)

    def test_base_view_template(self):
        self.assertEqual(BaseView.template_name, '')

    def test_index(self):
        request = self.factory.get('/')
        request.user = self.user
        response = views.IndexView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_home(self):
        request = self.factory.get('/home/')
        request.user = self.user
        response = views.IndexView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class PopularCategoriesViewTestCase(TestVlog):

    def test_popular_categories(self):
        request = self.factory.get('/home/categories/popular/')
        request.user = self.user
        response = views.PopularCategoriesView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class PopulatedTagsViewTestCase(TestVlog):

    def test_populated_tags(self):
        request = self.factory.get('/home/tags/popular/')
        request.user = self.user
        response = views.PopulatedTagsView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class PopularArticlesViewTestCase(TestVlog):

    def test_popular_articles(self):
        request = self.factory.get('/home/articles/popular/')
        request.user = self.user
        response = views.PopularArticlesView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class ArticlesViewTestCase(TestVlog):

    def test_articles(self):
        request = self.factory.get('/home/articles/')
        request.user = self.user
        response = views.ArticlesView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class CategoriesViewTestCase(TestVlog):

    def test_articles(self):
        request = self.factory.get('/home/categories/')
        request.user = self.user
        response = views.CategoriesView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class ArticleViewTestCase(TestVlog):

    def test_simple_load(self):
        instance = views.Article.objects.get(title='футбол')
        self.assertIsInstance(instance, views.Article)

    def test_article_view(self):
        article = views.Article.objects.get(title='тестовая статься')

        self.assertEqual(article.title, 'тестовая статься')
        self.assertEqual(article.slug, 'testovaya-statia')
        self.assertEqual(article.author, self.user)

    # def test_articles(self):
    #     request = self.factory.get(
    #         '/home/categories/football/articles/testovaya-statia)/'
    #     )
    #     request.user = self.user
    #     response = views.ArticleView.as_view()(request, 'football', 'testovaya-statia')
    #     self.assertEqual(response.status_code, 200)


class CategoryViewTestCase(TestVlog):

    def test_category_simple_load(self):
        instance = views.Category.objects.get(title='спорт')
        self.assertIsInstance(instance, views.Category)

    def test_category_view(self):
        category = views.Category.objects.get(title='абра-кадабра')

        self.assertEqual(category.title, 'абра-кадабра')
        self.assertEqual(category.slug, 'abra-kadabra')
        self.assertEqual(category.author, self.user)

    # def test_category(self):
    #     category = views.Category.objects.get(slug='sport')
    #     request = self.factory.get(
    #         '/home/categories/sport/'
    #     )
    #     request.user = self.user
    #     response = views.CategoryView.as_view()(request, category.slug)
    #     self.assertEqual(response.status_code, 200)


class TagsViewTestCase(TestVlog):

    def test_articles(self):
        request = self.factory.get('/home/tags/')
        request.user = self.user
        response = views.TagsView.as_view()(request)
        self.assertEqual(response.status_code, 200)


# class TagViewTestCase(TestVlog):

#     def test_articles(self):
#         request = self.factory.get('/home/tags/ball/')
#         request.user = self.user
#         response = views.TagView.as_view()(request)
#         self.assertEqual(response.status_code, 200)
