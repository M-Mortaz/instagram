from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from location import models
from . import serializers


class CityListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer


class CityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer


class CountryListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class CountryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class LocationListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        city = get_object_or_404(
            models.City, name=serializer.initial_data['city']['name']
        )
        country = get_object_or_404(
            models.Country, name=serializer.initial_data['country']['name']
        )
        models.Location.objects.create(city=city, country=country)
        headers = self.get_success_headers(serializer.data)
        return Response({'Message':'Created'}, status=status.HTTP_201_CREATED, headers=headers)


class LocationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer
