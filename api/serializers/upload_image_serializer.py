from rest_framework import serializers

from api.models.upload_image import UploadImage


class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = ("id", "name", "image", "thumbnail_image", "created_at", "modified_at")
        read_only_fields = ("thumbnail_image", "created_at", "modified_at")
