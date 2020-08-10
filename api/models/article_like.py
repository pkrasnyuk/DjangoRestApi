from django.contrib.auth.models import User
from django.db import models

from api.helpers.validators import alphanumeric
from api.models.article import Article
from api.models.base_model import BaseModel


class ArticleLike(BaseModel):
    article = models.ForeignKey(Article, blank=False, null=False, related_name='likes', on_delete=models.CASCADE)
    like = models.ForeignKey(User, blank=False, null=False, related_name='articles_like', on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True, validators=[alphanumeric])

    def __str__(self):
        return self.article.title

    class Meta:
        ordering = ('id',)
