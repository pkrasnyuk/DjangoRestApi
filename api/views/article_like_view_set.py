from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import viewsets, permissions
from rest_framework.filters import OrderingFilter
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api import serializers
from api.models.article_like import ArticleLike
from api.views.common import NoTitleAutoSchema, ConnectionValidations


class ArticleLikeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_class = [JSONWebTokenAuthentication, OAuth2Authentication]
    queryset = ArticleLike.objects.all().cache(ops=['get', 'fetch'], timeout=60 * 30) \
        if ConnectionValidations.redis_connection_validation() else ArticleLike.objects.all()
    serializer_class = serializers.ArticleLikeSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('article', 'like',)
    ordering_fields = ('created_at', 'modified_at',)
    ordering = ('created_at',)

    swagger_schema = NoTitleAutoSchema
