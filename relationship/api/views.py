from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from relationship import models
from . import serializers

User = get_user_model()

RESPONSE = Response({'Message': 'Not allowed'}, status=status.HTTP_403_FORBIDDEN)


class UserFollowers(generics.ListCreateAPIView):
    serializer_class = serializers.RelationSerializer

    def get_user(self):
        return get_object_or_404(
            User,
            username=self.kwargs['username']
        )

    def get_queryset(self):
        return models.Relation.objects.filter(
            to_user=self.get_user(), confirmation=True
        )

    def create(self, request, *args, **kwargs):
        from_user = request.user
        to_user = self.get_user()
        if not from_user == to_user:
            relation = models.Relation.objects.filter(
                from_user=from_user,
                to_user=to_user
            )
            if not relation.exists():
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save(
                    from_user=request.user,
                    to_user=self.get_user()
                )
                headers = self.get_success_headers(serializer.data)
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED, headers=headers
                )
            relation.first().delete()
        return Response({'Message': 'Done'})


class FollowRequests(generics.ListAPIView):
    serializer_class = serializers.RelationSerializer

    def get_user(self):
        return get_object_or_404(
            User,
            username=self.kwargs['username']
        )

    def get_queryset(self):
        return models.Relation.objects.filter(
            to_user=self.request.user,
            confirmation=False
        )

    def list(self, request, *args, **kwargs):
        if request.user == self.get_user():
            return super(FollowRequests, self).list(request, *args, **kwargs)
        return RESPONSE


class UserFollowRequest(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RelationSerializer
    model = models.Relation

    def get_user(self):
        return get_object_or_404(User,
                                 username=self.kwargs['username']
                                 )

    def get_request_follower(self):
        return get_object_or_404(User,
                                 username=self.kwargs['username2']
                                 )

    def get_object(self):
        return get_object_or_404(models.Relation,
                                 from_user=self.get_request_follower(),
                                 to_user=self.get_user(),
                                 confirmation=False
                                 )

    def check(self):
        if self.get_object().to_user == self.request.user:
            return True
        return False

    def retrieve(self, request, *args, **kwargs):
        if self.check():
            return super(UserFollowRequest, self).retrieve(request, *args, **kwargs)
        return RESPONSE

    def update(self, request, *args, **kwargs):
        if self.check():
            return super(UserFollowRequest, self).update(request, *args, **kwargs)
        return RESPONSE

    def destroy(self, request, *args, **kwargs):
        if self.check():
            return super(UserFollowRequest, self).destroy(request, *args, **kwargs)
        return RESPONSE


class UserFollowings(generics.ListAPIView):
    serializer_class = serializers.RelationSerializer

    def get_user(self):
        return get_object_or_404(
            User, username=self.kwargs['username']
        )

    def get_queryset(self):
        return models.Relation.objects.filter(
            from_user=self.get_user(),
            confirmation=True
        )

    def list(self, request, *args, **kwargs):
        if self.get_user().public_private:
            relation = models.Relation.objects.filter(
                Q(from_user=request.user, to_user=self.get_user(), confirmation=True) |
                Q(from_user=self.get_user(), to_user=request.user, confirmation=True)
            ).exists()
            if relation:
                return super(UserFollowings, self).list(request, *args, **kwargs)
            else:
                return RESPONSE
        return super(UserFollowings, self).list(request, *args, **kwargs)
