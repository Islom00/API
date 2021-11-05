from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import PostModel

User = get_user_model()


class PostModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ("id", "author", "title", "body", "created_at")


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")

