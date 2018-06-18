from core.views import BaseView
from .models import Article, Category, Tag
from django.db.models import Count


class IndexView(BaseView):
    template_name = 'vlog/index.tpl'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        articles = Article.objects.all()
        categories = Category.objects.get(title=articles[0].category)
        most_popular_categories = Category.objects.annotate(articles_count=Count('articles')).order_by('-articles_count')[:3]
        most_commented_articles = Article.objects.annotate(comment_count=Count('comments')).order_by('-comment_count')[:10]
        most_populated_tags = Tag.objects.annotate(num_articles=Count('articles')).order_by('-num_articles')[:10]

        context.update({
            'articles': articles,
            'categories': categories,
            'most_popular_categories': most_popular_categories,
            'most_commented_articles': most_commented_articles,
            'most_populated_tags': most_populated_tags
        })

        return context


class ArticleView(IndexView):
    template_name = 'vlog/article.tpl'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        article = Article.objects.get(slug=kwargs.get('slug'))
        category = Category.objects.get(title=article.category)

        context.update({
            'article': article,
            'category': category
        })

        return context


class CategoriesView(IndexView):
    template_name = 'vlog/categories.tpl'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.all()

        context.update({
            'categories': categories
        })

        return context


class CategoryView(IndexView):
    template_name = 'vlog/category.tpl'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # category = Category.objects.filter(slug=kwargs.get('slug'))
        # articles = Article.objects.annotate(category_slug=kwargs.get('slug')) #. order_by('-comment_count')
        category = Category.objects.get(slug=kwargs.get('slug'))
        articles = Article.objects.filter(category_id=category.id)

        context.update({
            'category': category,
            'articles': articles
        })

        return context


class TagsView(IndexView):
    template_name = 'vlog/tags.tpl'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tags = Tag.objects.all()

        context.update({
            'tags': tags
        })

        return context