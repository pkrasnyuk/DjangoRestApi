from rest_framework import serializers

from api.models.article import Article
from api.serializers.user_serializer import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):

    # creator = UserSerializer(read_only=True)
    # creator_id = serializers.PrimaryKeyRelatedField(source='creator', queryset=User.objects.all(), write_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["creator"] = UserSerializer(instance.creator).data
        return representation

    class Meta:
        model = Article
        # fields = ('id', 'title', 'body', 'creator', 'creator_id', 'created_at', 'modified_at')
        fields = ("id", "title", "body", "creator", "created_at", "modified_at")
        read_only_fields = ("created_at", "modified_at")
        extra_kwargs = {
            "body": {"help_text": "body serializer help_text"},
            "creator": {"default": serializers.CurrentUserDefault()},
        }
