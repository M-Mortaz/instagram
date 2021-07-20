from rest_framework.test import APISimpleTestCase
from django.urls import reverse, resolve
from user.api import views


class TestUrls(APISimpleTestCase):
    def test_register(self):
        url = reverse('user:user-api:register')
        self.assertEqual(resolve(url).func.view_class, views.UserRegister)

    def test_user_list(self):
        url = reverse('user:user-api:user-list')
        self.assertEqual(resolve(url).func.view_class, views.UserList)

    def test_user_delete_update_retrieve(self):
        url = reverse('user:user-api:retrieve-update-delete',args=['django'])
        self.assertEqual(resolve(url).func.view_class, views.UserRetrieveDeleteUpdate)
