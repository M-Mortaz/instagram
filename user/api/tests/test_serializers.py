from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework.test import APITestCase

from user.api.serializers import UserSerializer


class TestSerializer(APITestCase):

    def test_valid_serializer(self):
        data = {
            'first_name': 'django',
            'last_name': 'bingo',
            'username': 'django',
            'password': 'django',
            'email': 'django@django.com',
            'phone_number': '09302658144',
            'bio': 'This is a test',
            'public_private': False,
        }
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_serializer(self):
        data = {
            'first_name': 'django',
            'last_name': 'bingo',
            'username': '***',
            'password': 'django',
            'email': 'django',
            'phone_number': '093026581444444444',
            'bio': 'This is a test',
            'public_private': False,
        }
        serializer = UserSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(len(serializer.errors), 3)

    def test_valid_file(self):
        upload_file = open(f'{settings.MEDIA_ROOT}/sajad/profiles/sajad-2021-07-21_191114.650771.png', 'rb')
        data = {
            'username': 'django',
            'password': 'django',
            'email': 'django@django.com',
            'avatar': SimpleUploadedFile(upload_file.name, upload_file.read())
        }
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
