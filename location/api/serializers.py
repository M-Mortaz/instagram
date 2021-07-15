from rest_framework import serializers

from location import models


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = (
            'name',
        )


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = (
            'name',
        )


class LocationSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    country = CountrySerializer(read_only=True)

    class Meta:
        model = models.Location
        fields = (
            'city',
            'country',
        )
