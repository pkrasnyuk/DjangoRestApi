from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.models.upload_image import UploadImage
from api.serializers.upload_image_serializer import UploadImageSerializer


class ImageList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_class = [JSONWebTokenAuthentication, OAuth2Authentication]
    parser_classes = (MultiPartParser, FormParser,)
    queryset = UploadImage.objects.all()
    serializer_class = UploadImageSerializer


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_class = [JSONWebTokenAuthentication, OAuth2Authentication]
    parser_classes = (MultiPartParser, FormParser,)
    queryset = UploadImage.objects.all()
    serializer_class = UploadImageSerializer
