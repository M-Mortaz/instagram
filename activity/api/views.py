import uuid

from django.shortcuts import get_object_or_404

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
        return get_object_or_404(Post, slug=self.kwargs['slug'])

    def perform_create(self, serializer):
        slug = self.request.user.username + 'comment' + str(uuid.uuid4())
        serializer.save(
            user=self.request.user,
            slug=slug,
            post=self.get_post()
        )


class ReplyListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.CommentSerializer

    def get_comment(self):
        return get_object_or_404(models.Comment, slug=self.kwargs['slug'])

    def get_queryset(self):
        return models.Comment.objects.filter(reply_to=self.get_comment())

    def perform_create(self, serializer):
        comment = self.get_comment()
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
        return get_object_or_404(Post, slug=self.kwargs['slug'])

    def create(self, request, *args, **kwargs):
        like_post = models.LikePost.objects.filter(
            like__user=request.user,
            post=self.get_post())

        if not like_post.exists():
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
                            headers=headers)
        like_post.first().delete()
        return Response({'Message': 'Done'})


class CommentLikeListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.CommentLikeSerializer

    def get_comment(self):
        return get_object_or_404(models.Comment, slug=self.kwargs['slug'])

    def get_queryset(self):
        return models.LikeComment.objects.filter(comment=self.get_comment())

    def create(self, request, *args, **kwargs):
        like_comment = models.LikeComment.objects.filter(
            like__user=request.user,
            comment=self.get_comment())

        if not like_comment.exists():
            like = models.Like(user=request.user)
            like.save()
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(
                comment=self.get_comment(),
                like=like,
            )
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED,
                            headers=headers
                            )
        like_comment.first().delete()
        return Response({'Message': 'Done'})
