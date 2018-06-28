from core.views import BaseView
from .models import Article, Category, Tag
from django.db.models import Count

from django.core.paginator import Paginator
from django.urls import reverse
from django.utils.translation import gettext as _


class IndexView(BaseView):
    template_name = 'vlog/index.tpl'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        articles = Article.get_all()

        context.update({
            'articles': articles,
            'most_popular_categories': Category.objects.annotate(
                articles_count=Count('articles'))[:3],
            'most_commented_articles': Article.objects.annotate(
                comment_count=Count('comments'))[:3],
            'most_populated_tags': Tag.objects.annotate(
                num_articles=Count('articles'))[:3],
        })

        return context


class ArticlesView(IndexView):
    template_name = 'vlog/articles.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Home')},
        ]

        context.update({
            'crumbs': crumbs
        })

        return self.render_to_response(context)


class ArticleView(IndexView):
    template_name = 'vlog/article.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        article = Article.objects.get(slug=kwargs.get('article_slug'))
        category = Category.objects.get(title=article.category)

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Home')},
            {'url': reverse('vlog:categories'), 'title': _('Categories')},
            {'url': reverse('vlog:articles'), 'title': article.category.title},
        ]

        context.update({
            'crumbs': crumbs,
            'article': article,
            'category': category
        })

        return self.render_to_response(context)


class CategoriesView(IndexView):
    template_name = 'vlog/categories.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        categories_list = Category.objects.all()
        paginator = Paginator(categories_list, 2)

        page = request.GET.get('page')
        categories = paginator.get_page(page)

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Home')},
        ]

        context.update({
            'categories': categories,
            'paginator': paginator,
            'crumbs': crumbs
        })
        return self.render_to_response(context)


class CategoryView(IndexView):
    template_name = 'vlog/category.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        category = Category.objects.get(slug=kwargs.get('article_category_slug'))
        articles = Article.objects.filter(category=category)

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Home')},
            {'url': reverse('vlog:categories'), 'title': _('Categories')}
        ]

        context.update({
            'crumbs': crumbs,
            'category': category,
            'articles': articles
        })
        return self.render_to_response(context)


class TagsView(IndexView):
    template_name = 'vlog/tags.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        tags = Tag.objects.all()

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Home')},
        ]

        context.update({
            'crumbs': crumbs,
            'tags': tags
        })

        return self.render_to_response(context)


class TagView(IndexView):
    template_name = 'vlog/tag.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        tag = Tag.objects.get(slug=kwargs.get('slug'))
        articles = Article.objects.filter(tags=tag)

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Home')},
            {'url': reverse('vlog:tags'), 'title': _('Tags')}
        ]

        context.update({
            'crumbs': crumbs,
            'tag': tag,
            'articles': articles
        })
        return self.render_to_response(context)


class PopulatedTagsView(IndexView):
    template_name = 'vlog/populated_tags.tpl'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        populated_tags = Tag.objects.annotate(
            num_articles=Count('articles'))

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Home')},
            {'url': reverse('vlog:tags'), 'title': _('Tags')}
        ]

        context.update({
            'crumbs': crumbs,
            'populated_tags': populated_tags
        })

        return context


class PopularCategoriesView(IndexView):
    template_name = 'vlog/popular_categories.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        popular_categories = Category.objects.annotate(
            articles_count=Count('articles'))

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Home')},
            {'url': reverse('vlog:categories'), 'title': _('Categories')}
        ]

        context.update({
            'crumbs': crumbs,
            'popular_categories': popular_categories
        })

        return self.render_to_response(context)


class PopularArticlesView(IndexView):
    template_name = 'vlog/popular_articles.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        popular_articles = Article.objects.annotate(
            comment_count=Count('comments'))

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Home')},
            {'url': reverse('vlog:articles'), 'title': _('Articles')}
        ]

        context.update({
            'crumbs': crumbs,
            'popular_articles': popular_articles
        })

        return self.render_to_response(context)