from django.urls import re_path

from vlog import views

urlpatterns = [
    re_path('^$', views.IndexView.as_view(), name='index'),
    re_path('^home/$', views.IndexView.as_view(), name='index'),
    re_path('^home/categories/(?P<article_category_slug>\w+)/articles/(?P<article_slug>\w+)/', views.ArticlesView.as_view(template_name='vlog/article.tpl'), name='article'),
    re_path('^home/articles/', views.ArticlesView.as_view(template_name='vlog/articles.tpl'), name='articles'),
    re_path('^home/categories/$', views.CategoriesView.as_view(template_name='vlog/categories.tpl'), name='categories'),
    re_path('^home/categories/popular/$', views.PopularCategoriesView.as_view(template_name='vlog/popular_categories.tpl'), name='popular_categories'),
    re_path('^home/categories/(?P<slug>[\w-]+)/', views.CategoryView.as_view(template_name='vlog/category.tpl'), name='category'),
    re_path('^home/tags/popular/$', views.PopulatedTagsView.as_view(template_name='vlog/populated_tags.tpl'), name='populated_tags'),
    re_path('^home/tags/$', views.TagsView.as_view(template_name='vlog/tags.tpl'), name='tags'),
    re_path('^home/tags/(?P<slug>[\w-]+)/', views.TagView.as_view(template_name='vlog/tag.tpl'), name='tag'),
    re_path('^home/articles/popular/$', views.PopularArticlesView.as_view(template_name='vlog/popular_articles.tpl'), name='popular_articles'),
]