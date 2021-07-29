from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import test

from social.models import Post
from activity import models

User = get_user_model()


class TestActivityViews(test.APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='django',
            password='123456',
            email='django@django.com'
        )
        self.post = Post.objects.create(
            user=self.user,
            caption='Test from Django',
            slug='test-django-post'
        )
        self.comment = models.Comment.objects.create(
            user=self.user,
            content='This is a test from django',
            post=self.post,
            slug='main-comment-slug'
        )

        self.client = test.APIClient()

    def test_unauthorized_list_create_comment(self):
        request = self.client.post(reverse(
            'activity:activity-api:comment-list-create', args=['test-django-post']),
            {
                'user': self.user.id,
                'content': 'This is a test',
                'post': self.post.id,
                'slug': 'django-test2'
            })
        self.assertEqual(request.status_code, 401)

    def test_list_create_comment(self):
        self.client.force_authenticate(user=self.user)
        request = self.client.post(reverse(
            'activity:activity-api:comment-list-create', args=['test-django-post']),
            {
                'user': self.user.id,
                'content': 'This is a test',
                'post': self.post.id,
                'slug': 'django-test2'
            })
        request2 = self.client.get(reverse(
            'activity:activity-api:comment-list-create', args=['test-django-post']),
        )

        self.assertEqual(request.status_code, 201)
        self.assertEqual(request2.status_code, 200)
        self.assertEqual(models.Comment.objects.count(), 2)

    def test_unauthorized_reply_list_create(self):
        request = self.client.get(reverse(
            'activity:activity-api:reply-list-create',
            args=['main-comment-slug'])
        )
        self.assertEqual(request.status_code, 401)

    def test_reply_list_create(self):
        request = self.client.get(reverse(
            'activity:activity-api:reply-list-create',
            args=['main-comment-slug'])
        )
        self.client.force_authenticate(user=self.user)
        request1 = self.client.get(reverse(
            'activity:activity-api:reply-list-create',
            args=['main-comment-slug'])
        )
        request2 = self.client.post(reverse(
            'activity:activity-api:reply-list-create',
            args=['main-comment-slug']
        ),
            {
                'user': self.user,
                'content': 'This is a simple reply',
                'post': self.post,
                'slug': 'a simple reply_to slug'
            }
        )

        self.assertEqual(request1.status_code, 200)
        self.assertEqual(request2.status_code, 201)
        self.assertEqual(models.Comment.objects.exclude(reply_to=None).count(), 1)

    def test_comment_retrieve_update_delete(self):
        comment = models.Comment.objects.create(
            user=self.user,
            content='This is another test from django',
            post=self.post,
            slug='comment-slug'
        )
        self.client.force_authenticate(user=self.user)
        request = self.client.put(reverse(
            'activity:activity-api:comment-retrieve-update-delete', args=['comment-slug']),
            {
                'user': self.user,
                'content': 'changed',
                'post': self.post,
                'slug': 'changed-slug',
            }
        )
        self.assertTrue(request.status_code == 200)
        self.assertTrue(models.Comment.objects.filter(content='changed').exists())

        request2 = self.client.delete(reverse(
            'activity:activity-api:comment-retrieve-update-delete', args=[comment.slug]),
        )
        self.assertEqual(request2.status_code, 204)
        self.assertFalse(models.Comment.objects.filter(slug=comment.slug).exists())

    def test_post_like_list_create(self):
        self.client.force_authenticate(user=self.user)
        request = self.client.get(reverse(
            'activity:activity-api:like-post-list-create', args=[self.post.slug]),
        )
        request2 = self.client.post(reverse(
            'activity:activity-api:like-post-list-create', args=[self.post.slug]),
        )
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request2.status_code, 201)
        self.assertTrue(models.LikePost.objects.count() == 1)
        request3 = self.client.post(reverse(
            'activity:activity-api:like-post-list-create', args=[self.post.slug]),
        )
        self.assertTrue(models.LikePost.objects.count() == 0)
        self.assertEqual(request3.status_code, 200)

    def test_comment_like_list_create(self):
        self.client.force_authenticate(user=self.user)
        request = self.client.get(reverse(
            'activity:activity-api:like-comment-list-create', args=[self.comment.slug])
        )
        request2 = self.client.post(reverse(
            'activity:activity-api:like-comment-list-create', args=[self.comment.slug]),
        )

        self.assertEqual(request.status_code, 200)
        self.assertEqual(request2.status_code, 201)
        self.assertTrue(models.LikeComment.objects.count() == 1)

        request3 = self.client.post(reverse(
            'activity:activity-api:like-comment-list-create', args=[self.comment.slug]),
        )
        self.assertEqual(request3.status_code, 200)
        self.assertTrue(models.LikeComment.objects.count() == 0)
