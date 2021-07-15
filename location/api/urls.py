from django.urls import path

from . import views

urlpatterns = [
    path('city-list-create/',
         views.CityListCreate.as_view(), name='city-list-create'),

    path('city-retrieve-update-delete/<str:name>/',
         views.CityRetrieveUpdateDestroyAPIView.as_view(),
         name='city-retrieve-update-destroy'),

    path('country-list-create/',
         views.CountryListCreate.as_view(), name='country-list-create'),

    path('country-retrieve-update-delete/<str:name>/',
         views.CountryRetrieveUpdateDestroyAPIView.as_view(),
         name='country-retrieve-update-destroy'),

    path('location-list-create/',
         views.LocationListCreate.as_view(), name='location-list-create'),

    path('location-retrieve-update-delete/<str:name>/',
         views.LocationRetrieveUpdateDestroyAPIView.as_view(),
         name='location-retrieve-update-destroy')
]
