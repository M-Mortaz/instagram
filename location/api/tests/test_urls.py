from django.urls import resolve, reverse

from rest_framework.test import APISimpleTestCase

from location.api import views


class TestUrls(APISimpleTestCase):

    def test_city_list_create(self):
        url = reverse('location:location-api:city-list-create')
        self.assertEqual(resolve(url).func.view_class, views.CityListCreate)

    def test_city_retrieve_update_delete(self):
        url = reverse('location:location-api:city-retrieve-update-destroy', args=['django'])
        self.assertEqual(resolve(url).func.view_class, views.CityRetrieveUpdateDestroyAPIView)

    def test_country_list_create(self):
        url = reverse('location:location-api:country-list-create')
        self.assertEqual(resolve(url).func.view_class, views.CountryListCreate)

    def test_country_retrieve_update_delete(self):
        url = reverse('location:location-api:country-retrieve-update-destroy', args=['django'])
        self.assertEqual(resolve(url).func.view_class, views.CountryRetrieveUpdateDestroyAPIView)

    def test_location_list_create(self):
        url = reverse('location:location-api:location-list-create')
        self.assertEqual(resolve(url).func.view_class, views.LocationListCreate)

    def test_location_retrieve_update_delete(self):
        url = reverse('location:location-api:location-retrieve-update-destroy', args=[1])
        self.assertEqual(resolve(url).func.view_class, views.LocationRetrieveUpdateDestroyAPIView)
