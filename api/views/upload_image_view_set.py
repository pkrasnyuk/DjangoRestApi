from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.serializers.upload_image_serializer import UploadImageSerializer


class UploadImageViewSet(RetrieveAPIView):
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (AllowAny,)
    serializer_class = UploadImageSerializer
    http_method_names = ['post']

    @swagger_auto_schema(operation_description='Upload file...', )
    @action(detail=False, methods=['post'])
    def post(self, request):
        file_serializer = UploadImageSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
