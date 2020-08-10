from django.contrib import admin

from .models.article import Article
from .models.article_like import ArticleLike
from .models.snippet import Snippet
from .models.upload_image import UploadImage

# Register your models here.
admin.site.register(Article)
admin.site.register(ArticleLike)
admin.site.register(Snippet)
admin.site.register(UploadImage)
