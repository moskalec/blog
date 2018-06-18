from django.urls import re_path

from vlog import views

urlpatterns = [
    re_path('^$', views.IndexView.as_view(), name='index'),
    re_path('^categories/$', views.CategoriesView.as_view(), name='categories'),
    re_path('^tags/$', views.TagsView.as_view(), name='tags')
]