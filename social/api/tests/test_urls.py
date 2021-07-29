from django.urls import resolve, reverse
from rest_framework.test import APISimpleTestCase

from social.api import views


class TestUrls(APISimpleTestCase):
    def test_get_update_delete(self):
        url = reverse('social:social-api:get-update-delete', args=['django'])
        self.assertEqual(resolve(url).func.view_class, views.PostRetrieveUpdateDestroy)

    def test_list_create(self):
        url = reverse('social:social-api:list-create')
        self.assertEqual(resolve(url).func.view_class, views.PostListCreate)

    def test_media_list_create(self):
        url = reverse('social:social-api:media-list-create', args=['django'])
        self.assertEqual(resolve(url).func.view_class, views.PostMediaView)
