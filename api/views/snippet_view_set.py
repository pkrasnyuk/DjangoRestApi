from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import permissions, generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.models.snippet import Snippet
from api.serializers.snippet_serializer import SnippetSerializer
from api.views.common import ConnectionValidations


class SnippetList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_class = [JSONWebTokenAuthentication, OAuth2Authentication]
    queryset = Snippet.objects.all().cache(ops=['get', 'fetch'], timeout=60 * 30) \
        if ConnectionValidations.redis_connection_validation() else Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_class = [JSONWebTokenAuthentication, OAuth2Authentication]
    queryset = Snippet.objects.all().cache(ops=['get', 'fetch'], timeout=60 * 30) \
        if ConnectionValidations.redis_connection_validation() else Snippet.objects.all()
    serializer_class = SnippetSerializer
