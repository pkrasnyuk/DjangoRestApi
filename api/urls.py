from django.conf.urls import include, url
from django.urls import path
from rest_framework.routers import SimpleRouter

from api import views

router = SimpleRouter()
router.register(r'articles', views.ArticleViewSet)
router.register(r'article_likes', views.ArticleLikeViewSet)

urlpatterns = [
    url('', include(router.urls)),
    path('articles/', include(([
                                   path('creator/<int:creator_pk>/',
                                        views.article_view_set.CreatorArticleViewSet.as_view()),
                               ], 'api'), namespace='articles')),
    path('snippets/', include(([
                                   path('', views.snippet_view_set.SnippetList.as_view()),
                                   path('<int:pk>/', views.snippet_view_set.SnippetDetail.as_view()),
                               ], 'api'), namespace='snippets')),
    path('users/', include(([
                                path('', views.user_view_set.UserList.as_view()),
                                path('<int:pk>/', views.user_view_set.UserDetail.as_view()),
                                path('signup/', views.UserLoginViewSet.as_view()),
                            ], 'api'), namespace='users')),
    path('upload/', views.UploadImageViewSet.as_view(), name='upload'),
    path('images/', include(([
                                 path('', views.image_view_set.ImageList.as_view()),
                                 path('<int:pk>/', views.image_view_set.ImageDetail.as_view()),
                             ], 'api'), namespace='images')),
]
