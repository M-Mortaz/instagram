from django.contrib import admin
from . import models


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = 'name',


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = 'name',


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    pass