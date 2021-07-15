import uuid
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from activity import models
from social.models import Post
from . import serializers


class CommentListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        return models.Comment.objects.filter(post=self.get_post())

    def get_post(self):
        return Post.objects.get(slug=self.kwargs['slug'])

    def perform_create(self, serializer):
        slug = self.request.user.username + 'comment' + str(uuid.uuid4())
        serializer.save(
            user=self.request.user,
            slug=slug,
            post=self.get_post()
        )


class ReplyListCreate(generics.ListCreateAPIView):
    model = models.Comment
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        comment = self.get_object()
        return models.Comment.objects.filter(reply_to=comment)

    def perform_create(self, serializer):
        comment = self.get_object()
        slug = self.request.user.username + 'reply' + str(uuid.uuid4())
        serializer.save(
            user=comment.user,
            slug=slug,
            post=comment.post,
            reply_to=comment
        )


class CommentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    model = models.Comment
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class PostLikeListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.PostLikeSerializer

    def get_queryset(self):
        return models.LikePost.objects.filter(
            post=self.get_post()
        )

    def get_post(self):
        return Post.objects.get(slug=self.kwargs['slug'])

    def create(self, request, *args, **kwargs):
        if not models.LikePost.objects.filter(
                like__user=request.user,
                post=self.get_post()
        ).exists():
            like = models.Like(user=request.user)
            like.save()
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(
                post=self.get_post(),
                like=like
            )
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED,
                            headers=headers
                            )
        like_post = models.LikePost.objects.filter(
            like__user=request.user,
            post=self.get_post()
        ).first()
        like_post.like.delete()
        return Response({'Message': 'Done'})
