from django.urls import reverse, resolve
from rest_framework.test import APISimpleTestCase

from activity.api import views


class TestUrls(APISimpleTestCase):

    def test_comment_list_create(self):
        url = reverse('activity:activity-api:comment-lc', args=['django'])
        self.assertEqual(resolve(url).func.view_class, views.CommentListCreate)

    def test_comment_retrieve_update_delete(self):
        url = reverse('activity:activity-api:comment-rud', args=['django'])
        self.assertEqual(resolve(url).func.view_class, views.CommentRetrieveUpdateDestroy)

    def test_comment_reply(self):
        url = reverse('activity:activity-api:reply-create', args=['django'])
        self.assertEqual(resolve(url).func.view_class, views.ReplyListCreate)

    def test_like_post_list_create(self):
        url = reverse('activity:activity-api:like-plc', args=['django'])
        self.assertEqual(resolve(url).func.view_class, views.PostLikeListCreate)

    def test_like_comment_list_create(self):
        url = reverse('activity:activity-api:like-clc', args=['django'])
        self.assertEqual(resolve(url).func.view_class, views.CommentLikeListCreate)
