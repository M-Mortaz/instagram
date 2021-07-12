from rest_framework import serializers

from social import models
from user.api.serializers import UserSerializer


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Media
        fields = (
            'media',
        )


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    media = MediaSerializer(required=False, many=True)

    class Meta:
        model = models.Post
        fields = (
            'user',
            'caption',
            'media',
            'location',
            'allow_share',
        )

        extra_kwargs = {
            'caption': {'required': False},
            'location': {'required': False},
        }
