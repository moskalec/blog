from django.urls import re_path

from vlog import views

urlpatterns = [
    re_path('^$', views.IndexView.as_view(), name='index'),

    re_path(
        '^home/$', views.IndexView.as_view(), name='index'
    ),

    re_path(
        '^home/categories/popular/$',
            views.PopularCategoriesView.as_view(), name='popular_categories'
    ),

    re_path(
        '^home/tags/popular/$',
            views.PopulatedTagsView.as_view(), name='populated_tags'
    ),

    re_path(
        '^home/articles/popular/$',
            views.PopularArticlesView.as_view(), name='popular_articles'
    ),

    re_path(
        '^home/articles/', views.ArticlesView.as_view(), name='articles'
    ),

    re_path(
        '^home/categories/$', views.CategoriesView.as_view(), name='categories'
    ),

    re_path(
        "^home/categories/(?P<article_category_slug>[\w-]+[']*)"
            "/articles/(?P<article_slug>[\w-]+[']*)/",
            views.ArticleView.as_view(), name='article'
    ),

    re_path(
        "^home/categories/(?P<article_category_slug>[\w-]+[']*)/",
            views.CategoryView.as_view(), name='category'
    ),

    re_path(
        '^home/tags/$', views.TagsView.as_view(), name='tags'
    ),

    re_path(
        "^home/tags/(?P<slug>[\w-]+[']*)/", views.TagView.as_view(), name='tag'
    ),
]