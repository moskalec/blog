from django.urls import re_path

from vlog import views

urlpatterns = [
    re_path('^$', views.IndexView.as_view(), name='index'),
    re_path('^home/$', views.IndexView.as_view(), name='index'),
    re_path('^home/categories/$', views.CategoriesView.as_view(template_name='vlog/categories.tpl'), name='categories'),
    re_path('^home/categories/(?P<slug>[\w-]+)/$', views.CategoryView.as_view(template_name='vlog/category.tpl'), name='category'),
    re_path('^home/tags/$', views.TagsView.as_view(template_name='vlog/tags.tpl'), name='tags'),
    re_path('^home/tags/(?P<slug>[\w-]+)/$', views.TagView.as_view(template_name='vlog/tag.tpl'), name='tag'),
    re_path('^home/articles/', views.ArticlesView.as_view(template_name='vlog/articles.tpl'), name='articles'),
    re_path('^home/articles/(?P<slug>[\w-]+)/', views.ArticleView.as_view(template_name='vlog/article.tpl')),
]