from core.views import BaseView
from .models import Article, Category, Tag
from django.db.models import Count

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render


class IndexView(BaseView):
    template_name = 'vlog/index.tpl'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        articles = Article.objects.all()

        categories = Category.objects.get(title=articles[0].category)

        most_popular_categories = Category.objects\
                            .annotate(articles_count=Count('articles'))\
                            .order_by('-articles_count')[:3]

        most_commented_articles = Article.objects\
                            .annotate(comment_count=Count('comments'))\
                            .order_by('-comment_count')[:3]

        most_populated_tags = Tag.objects\
                            .annotate(num_articles=Count('articles'))\
                            .order_by('-num_articles')[:3]

        context.update({
            'articles': articles,
            'categories': categories,
            'most_popular_categories': most_popular_categories,
            'most_commented_articles': most_commented_articles,
            'most_populated_tags': most_populated_tags
        })

        return context


class ArticlesView(IndexView):
    template_name = 'vlog/articles.tpl'


class ArticleView(IndexView):
    template_name = 'vlog/article.tpl'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        article = Article.objects.get(slug=kwargs.get('article_title'))
        category = Category.objects.get(title=article.category)

        context.update({
            'article': article,
            'category': category
        })

        return context


class CategoriesView(IndexView):
    template_name = 'vlog/categories.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        categories_list = Category.objects.all()
        paginator = Paginator(categories_list, 2)

        page = request.GET.get('page')
        categories = paginator.get_page(page)

        context.update({
            'categories': categories
        })
        # import ipdb
        # ipdb.set_trace()
        return self.render_to_response(context)


class CategoryView(IndexView):
    template_name = 'vlog/category.tpl'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category = Category.objects.get(slug=kwargs.get('slug'))
        articles = Article.objects.filter(category=category)

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


class TagView(IndexView):
    template_name = 'vlog/tag.tpl'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tag = Tag.objects.get(slug=kwargs.get('slug'))
        articles = Article.objects.filter(tags=tag)

        context.update({
            'tag': tag,
            'articles': articles
        })

        return context


class PopulatedTagsView(IndexView):
    template_name = 'vlog/populated_tags.tpl'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        popular_tags = Tag.objects.annotate(num_articles=Count('articles'))\
                                            .order_by('-num_articles')

        context.update({
            'popular_tags': popular_tags
        })

        return context


class PopularCategoriesView(IndexView):
    template_name = 'vlog/popular_categories.tpl'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        popular_categories = Category.objects\
                                .annotate(articles_count=Count('articles'))\
                                .order_by('-articles_count')

        context.update({
            'popular_categories': popular_categories
        })

        return context


class PopularArticlesView(IndexView):
    template_name = 'vlog/popular_articles.tpl'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        popular_articles = Article.objects\
                            .annotate(comment_count=Count('comments'))\
                            .order_by('-comment_count')

        context.update({
            'popular_articles': popular_articles
        })

        return context