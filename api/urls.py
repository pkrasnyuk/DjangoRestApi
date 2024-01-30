from django.conf.urls import include, url
from django.urls import path
from rest_framework.routers import SimpleRouter

from api.views import (
    article_like_view_set,
    article_view_set,
    image_view_set,
    snippet_view_set,
    upload_image_view_set,
    user_view_set,
)
from api.views.user_login_view_set import UserLoginViewSet

router = SimpleRouter()
router.register(r"articles", article_view_set.ArticleViewSet)
router.register(r"article_likes", article_like_view_set.ArticleLikeViewSet)

urlpatterns = [
    url("", include(router.urls)),
    path(
        "articles/",
        include(
            (
                [
                    path("creator/<int:creator_pk>/", article_view_set.CreatorArticleViewSet.as_view()),
                ],
                "api",
            ),
            namespace="articles",
        ),
    ),
    path(
        "snippets/",
        include(
            (
                [
                    path("", snippet_view_set.SnippetList.as_view()),
                    path("<int:pk>/", snippet_view_set.SnippetDetail.as_view()),
                ],
                "api",
            ),
            namespace="snippets",
        ),
    ),
    path(
        "users/",
        include(
            (
                [
                    path("", user_view_set.UserList.as_view()),
                    path("<int:pk>/", user_view_set.UserDetail.as_view()),
                    path("signup/", UserLoginViewSet.as_view()),
                ],
                "api",
            ),
            namespace="users",
        ),
    ),
    path("upload/", upload_image_view_set.UploadImageViewSet.as_view(), name="upload"),
    path(
        "images/",
        include(
            (
                [
                    path("", image_view_set.ImageList.as_view()),
                    path("<int:pk>/", image_view_set.ImageDetail.as_view()),
                ],
                "api",
            ),
            namespace="images",
        ),
    ),
]
