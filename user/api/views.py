from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from . import serializers

User = get_user_model()


class UserList(generics.ListAPIView):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()


class UserRegister(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.UserSerializer
    model = User


class UserRetrieveDeleteUpdate(generics.RetrieveUpdateDestroyAPIView):
    slug_field = 'username'
    slug_url_kwarg = 'username'
    lookup_field = 'username'

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def perform_update(self, serializer):  # Hashes the password before update
        try:
            password = serializer.initial_data['password']
            serializer.save(password=make_password(password))  # Sets the hashed password
        except:
            serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Done'}, status=status.HTTP_200_OK)
