from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings

from rest_framework.test import APITestCase

from social.api import serializers

User = get_user_model()


class TestMediaSerializer(APITestCase):

    def test_valid_data(self):
        upload_file = open(f'{settings.MEDIA_ROOT}/sajad/profiles/sajad-2021-07-21_191114.650771.png', 'rb')
        data = {
            'media': SimpleUploadedFile(upload_file.name, upload_file.read())
        }
        serializer = serializers.MediaSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_data(self):
        data = {
            'media': 'hello'
        }
        serializer = serializers.MediaSerializer(data=data)
        self.assertFalse(serializer.is_valid())


class TestPostSerializer(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='django',
            password='123456',
            email='django@django.com'
        )

    def test_valid_data(self):
        data = {
            'user': self.user,
            'slug': 'django'
        }
        serializer = serializers.PostSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_data(self):
        data = {
            'slug': 'django Python',
            'allow_share': ''
        }
        serializer = serializers.PostSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(len(serializer.errors), 2)
