from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase

from relationship.api import serializers

User = get_user_model()


class TestSerializer(APITestCase):

    def test_valid_data(self):
        user_1 = User.objects.create_user(
            username='django',
            password='123456',
            email='django@django.com',
        )
        user_2 = User.objects.create_user(
            username='django2',
            password='123456',
            email='django2@django.com',
        )
        data = {'from_user': user_1, 'to_user': user_2}
        serializer = serializers.RelationSerializer(data=data)
        self.assertTrue(serializer.is_valid())
