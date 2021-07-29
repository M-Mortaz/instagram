from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.conf import settings

from rest_framework import test

from social import models

User = get_user_model()


class TestSocialViews(test.APITestCase):

    def setUp(self):
        self.client = test.APIClient()
        self.user = User.objects.create(
            username='django',
            email='django@django.com',
            password='123456'
        )
        self.post = models.Post.objects.create(
            user=self.user,
            caption='django caption',
            slug='main-django-slug'
        )

    def test_list_create(self):
        self.client.force_authenticate(user=self.user)

        # List
        request = self.client.get(reverse(
            'social:social-api:list-create')
        )
        self.assertEqual(request.status_code, 200)

        # Create
        request2 = self.client.post(reverse(
            'social:social-api:list-create'),
            {
                'caption': 'This is a test from django'
            }
        )

        self.assertEqual(request2.status_code, 201)
        self.assertTrue(models.Post.objects.count() == 2)

    def test_retrieve_update_destroy(self):
        self.client.force_authenticate(user=self.user)

        post = models.Post.objects.create(
            user=self.user,
            caption='django caption2',
            slug='django2-slug'
        )

        # Retrieve
        request = self.client.get(reverse(
            'social:social-api:get-update-delete', args=[post.slug]),
        )
        self.assertTrue(request.status_code == 200)
        self.assertTrue(models.Post.objects.count() == 2)

        # Update
        request2 = self.client.patch(reverse(
            'social:social-api:get-update-delete', args=[post.slug]),
            {
                'caption': 'This is the changed caption'
            }
        )
        self.assertEqual(request2.status_code, 200)

        # Delete
        request3 = self.client.delete(reverse(
            'social:social-api:get-update-delete', args=[post.slug]),
        )

        self.assertTrue(request3.status_code, 204)
        self.assertTrue(models.Post.objects.count() == 1)

    def test_post_media(self):
        self.client.force_authenticate(user=self.user)
        file = open(f'{settings.MEDIA_ROOT}/sajad/profiles/sajad-2021-07-21_191114.650771.png', 'rb')

        # Create
        request = self.client.post(reverse(
            'social:social-api:media-list-create', args=[self.post.slug]),
            {
                'media': SimpleUploadedFile(file.name, file.read())
            }
        )
        self.assertTrue(request.status_code, 201)
        self.assertTrue(models.Post.objects.first().media.count() == 1)

        # get
        request2 = self.client.get(reverse(
            'social:social-api:media-list-create', args=[self.post.slug]),
        )
        self.assertTrue(request2.status_code, 200)
