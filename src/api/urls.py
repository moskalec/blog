from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
router.register(r'categories', views.CategoriesViewSet)
router.register(r'articles', views.ArticleViewSet)
router.register(r'tags', views.TagViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
