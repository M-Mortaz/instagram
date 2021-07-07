from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password',
            'email',
            'phone_number',
            'bio',
            'avatar',
            'public_private',
        )

        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True},
            'first_name': {'required': False},
            'last_name': {'required': False},
            'bio': {'required': False},
            'phone_number': {'required': False},
        }
