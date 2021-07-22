from django.contrib.auth import get_user_model

from relationship.models import Relation
from rest_framework.test import APITestCase

User = get_user_model()


class TestRelation(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username='django',
            password='1234560',
            email='django@django.com'
        )

        self.user2 = User.objects.create_user(
            username='django2',
            password='1234560',
            email='django2@django.com'
        )

    def test_create_valid_relation(self):
        try:
            Relation.objects.create(
                from_user=self.user1,
                to_user=self.user2,
            )
        except:
            pass

        self.assertEqual(Relation.objects.count(), 1)

    def test_create_invalid_relation(self):
        try:
            Relation.objects.create(
                from_user=self.user1,
                to_user=self.user1,
            )
        except:
            pass

        self.assertEqual(Relation.objects.count(), 0)
