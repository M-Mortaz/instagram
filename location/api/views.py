from django.shortcuts import get_object_or_404
from django.db import transaction

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
    lookup_field = 'name'
    lookup_url_kwarg = 'name'
    permission_classes = [permissions.IsAdminUser]
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer


class CountryListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class CountryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'name'
    lookup_url_kwarg = 'name'
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
        return Response({'Message': 'Created'}, status=status.HTTP_201_CREATED, headers=headers)


class LocationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        city = data.get('city')
        country = data.get('country')
        with transaction.atomic():
            if city is not None:
                instance.city = get_object_or_404(models.City, name=city['name'])
            if country is not None:
                instance.country = get_object_or_404(models.Country, name=country['name'])
            instance.save()
        return Response({'message': 'ok'})
