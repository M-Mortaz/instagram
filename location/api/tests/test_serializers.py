from rest_framework.test import APITestCase

from location.api import serializers

from location import models


class TestSerializer(APITestCase):

    def setUp(self):
        self.city = models.City.objects.create(name='Python')
        self.country = models.Country.objects.create(name='Django')

    def test_valid_city_serializer(self):
        data = {
            'name': 'django'
        }
        serializer = serializers.CitySerializer(data=data)
        if not serializer.is_valid():
            print(serializer.errors)
        self.assertTrue(serializer.is_valid())

    def test_invalid_city_serializer(self):
        data = {
            'name': ''
        }
        serializer = serializers.CitySerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_valid_country_serializer(self):
        data = {
            'name': 'django'
        }
        serializer = serializers.CountrySerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_country_serializer(self):
        data = {
            'name': ''
        }
        serializer = serializers.CountrySerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_valid_location(self):
        data = {
            'city': self.city,
            'country': self.country,
        }
        serializer = serializers.LocationSerializer(data=data)
        self.assertTrue(serializer.is_valid())
