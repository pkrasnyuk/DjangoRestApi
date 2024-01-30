from rest_framework import serializers

from api.models.article_like import ArticleLike
from api.serializers.article_serializer import ArticleSerializer
from api.serializers.user_serializer import UserSerializer


class ArticleLikeSerializer(serializers.ModelSerializer):

    # like = serializers.CharField(read_only=True)
    # like = UserSerializer(read_only=True)
    # article = serializers.CharField(read_only=True)
    # article = ArticleSerializer(read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["like"] = UserSerializer(instance.like).data
        representation["article"] = ArticleSerializer(instance.article).data
        return representation

    class Meta:
        model = ArticleLike
        fields = ("article", "like", "comment", "created_at", "modified_at")
        read_only_fields = ("created_at", "modified_at")
        extra_kwargs = {
            "article": {"default": serializers.CurrentUserDefault()},
            "like": {"default": serializers.CurrentUserDefault()},
            "comment": {"help_text": "comment serializer help_text"},
        }
