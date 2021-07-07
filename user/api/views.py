from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from . import serializers

User = get_user_model()


class UserRegister(generics.ListCreateAPIView):
    serializer_class = serializers.UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(**serializer.validated_data)
            return Response({'message': 'Okay'}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response({'message': 'Error'}, status=status.HTTP_400_BAD_REQUEST)
