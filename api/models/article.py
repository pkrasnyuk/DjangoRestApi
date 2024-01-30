from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from api.helpers.validators import alphanumeric
from api.models.base_model import BaseModel


class Article(BaseModel):
    title = models.CharField(
        help_text="title model help_text",
        max_length=255,
        blank=False,
        null=False,
        validators=[alphanumeric, MinLengthValidator(10)],
    )
    body = models.TextField(
        help_text="article model help_text",
        max_length=2048,
        blank=False,
        null=False,
        validators=[MinLengthValidator(15)],
    )
    creator = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name="articles")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("id",)
