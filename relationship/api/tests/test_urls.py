from django.urls import reverse, resolve
from rest_framework.test import APISimpleTestCase

from relationship.api import views


class TestUrls(APISimpleTestCase):

    def test_user_followers(self):
        url = reverse('relationship:relationship-api:followers', args=['django'])
        self.assertEqual(resolve(url).func.view_class, views.UserFollowers)

    def test_follow_requests(self):
        url = reverse('relationship:relationship-api:requests', args=['django'])
        self.assertEqual(resolve(url).func.view_class, views.FollowRequests)

    def test_user_follow_request(self):
        url = reverse('relationship:relationship-api:user-request', args=['django', 'django'])
        self.assertEqual(resolve(url).func.view_class, views.UserFollowRequest)

    def test_user_followings(self):
        url = reverse('relationship:relationship-api:followings', args=['django'])
        self.assertEqual(resolve(url).func.view_class, views.UserFollowings)
