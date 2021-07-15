from rest_framework import serializers

from activity import models
from user.api import serializers as user_serializers
from social.api import serializers as post_serializer


class LikeSerializer(serializers.ModelSerializer):
    user = user_serializers.UserSerializer(read_only=True)

    class Meta:
        model = models.Like
        fields = (
            'user',
        )


class PostLikeSerializer(serializers.ModelSerializer):
    post = post_serializer.PostSerializer(read_only=True)
    like = LikeSerializer()

    class Meta:
        model = models.LikePost
        fields = (
            'like',
            'post',
        )


class CommentSerializer(serializers.ModelSerializer):
    user = user_serializers.UserSerializer(read_only=True)
    post = post_serializer.PostSerializer(read_only=True)

    class Meta:
        model = models.Comment
        fields = (
            'user',
            'post',
            'content',
            'slug',
        )

        extra_kwargs = {
            'slug': {'read_only': True},
        }

    def get_fields(self):
        fields = super().get_fields()
        fields['reply_to'] = CommentSerializer(read_only=True)
        return fields
