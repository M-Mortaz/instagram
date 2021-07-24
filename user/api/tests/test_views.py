from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase, APIClient

User = get_user_model()


class TestRegisterView(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(
            username='django',
            password='123456',
            email='django@django.com'
        )

    def test_register_valid_POST(self):
        request = self.client.post(reverse('user:user-api:register'), {
            'username': 'django1',
            'email': 'django1@django.com',
            'password': '123456'
        })
        self.assertEqual(request.status_code, 201)
        self.assertEqual(User.objects.count(), 2)

    def test_register_invalid_POST(self):
        request = self.client.post(reverse('user:user-api:register'), {
            'username': '****',
            'email': 'django',
            'password': ''
        })
        self.assertEqual(request.status_code, 400)
        self.assertEqual(User.objects.count(), 1)

    def test_users_list_GET(self):
        self.client.force_authenticate(user=self.user)
        request = self.client.get(reverse('user:user-api:user-list'))
        self.assertEqual(request.status_code, 200)
        self.assertTrue(User.objects.count() == 1)

    def test_users_list_invalid_GET(self):
        request = self.client.get(reverse('user:user-api:user-list'))
        self.assertEqual(request.status_code, 401)

    def test_user_retrieve_GET(self):
        self.client.force_authenticate(user=self.user)
        request = self.client.get(reverse('user:user-api:retrieve-update-delete', args=['django']))
        self.assertEqual(request.status_code, 200)
        self.assertEqual(self.user.username, 'django')

    def test_user_retrieve_unauthorized_GET(self):
        request = self.client.get(reverse('user:user-api:retrieve-update-delete', args=['django']))
        self.assertEqual(request.status_code, 401)
        self.assertEqual(self.user.username, 'django')

    def test_update_user_invalid_PATCH(self):
        self.client.force_authenticate(user=self.user)
        request = self.client.patch(
            reverse('user:user-api:retrieve-update-delete', args=['django']),
            {'username': '****', 'password': '123456', 'admin': 'admin@admin.com'}
        )
        self.assertEqual(request.status_code, 400)

    def test_update_user_valid_PATCH(self):
        self.client.force_authenticate(user=self.user)
        request = self.client.patch(
            reverse('user:user-api:retrieve-update-delete', args=['django']),
            {'username': 'admin', 'password': '123456', 'admin': 'admin@admin.com'}
        )
        self.assertEqual(request.status_code, 200)

    def test_destroy_user_DELETE(self):
        self.client.force_authenticate(user=self.user)
        request = self.client.delete(
            reverse('user:user-api:retrieve-update-delete', args=['django'])
        )
        self.assertEqual(request.status_code, 200)
        self.assertEqual(User.objects.count(), 0)
