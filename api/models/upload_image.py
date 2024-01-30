import os
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django_cleanup import cleanup
from PIL import Image

from api.helpers.image_helper import nameFile
from api.models.base_model import BaseModel


@cleanup.ignore
class UploadImage(BaseModel):
    name = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to=nameFile, max_length=254, blank=True, null=True)
    thumbnail_image = models.ImageField(upload_to=nameFile, max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

    def create_thumbnail(self, thumbnails=[]):
        image = Image.open(self.image.file.file)
        file_name, ext = os.path.splitext(self.image.name)
        for w, h in thumbnails:
            image.thumbnail(size=(w, h))
            image_file = BytesIO()
            image.save(image_file, image.format)
            self.thumbnail_image.save(
                f"{file_name}_{w}x{h}{ext}",
                InMemoryUploadedFile(
                    image_file,
                    None,
                    "",
                    self.image.file.content_type,
                    image.size,
                    self.image.file.charset,
                ),
                save=False,
            )

    def save(self, *args, **kwargs):
        if not self.thumbnail_image:
            self.create_thumbnail(thumbnails=[(128, 128)])
        super().save(*args, **kwargs)

    class Meta:
        ordering = ("id",)
