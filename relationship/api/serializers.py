from rest_framework import serializers

from user.api import serializers as user_serializer
from relationship import models


class RelationSerializer(serializers.ModelSerializer):
    from_user = user_serializer.UserSerializer(read_only=True)
    to_user = user_serializer.UserSerializer(read_only=True)

    class Meta:
        model = models.Relation
        fields = (
            'from_user',
            'to_user',
            'confirmation',
            'created'
        )
