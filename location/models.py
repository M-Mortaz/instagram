from django.db import models
from django.utils.translation import ugettext_lazy as _

from lib import shared_models


class City(shared_models.BaseModel):
    name = models.CharField(_('name'), max_length=30,unique=True)

    class Meta:
        verbose_name        = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        return self.name


class Country(shared_models.BaseModel):
    name = models.CharField(_('name'), max_length=30,unique=True)

    class Meta:
        verbose_name        = _('Country')
        verbose_name_plural = _('Countries')

    def __str__(self):
        return self.name


class Location(shared_models.BaseModel):
    city    = models.OneToOneField(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
                                related_name='location')

    def __str__(self):
        return f"{self.city} ---> {self.country}"

    class Meta:
        verbose_name        = _('Location')
        verbose_name_plural = _('Locations')

