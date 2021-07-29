import uuid

from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from social import models


class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PostSerializer

    def get_object(self):
        return get_object_or_404(models.Post, slug=self.kwargs['slug'])


class PostListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()

    def perform_create(self, serializer):
        slug = self.request.user.username + 'post' + str(uuid.uuid4())
        serializer.save(user=self.request.user, slug=slug)


class PostMediaView(generics.CreateAPIView):
    serializer_class = serializers.MediaSerializer
    queryset = models.Media.objects.all()

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(models.Post, slug=kwargs['slug'])
        if request.user != post.user:
            return Response({'status': 'not allowed'}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, post=post)
        return Response({'status': 'Created'}, status=status.HTTP_201_CREATED)
