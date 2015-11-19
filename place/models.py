# coding=utf-8
from django.core.urlresolvers import reverse
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __unicode__(self):
        return u'{}'.format(self.name)

    def get_absolute_url(self):
         return reverse('country', kwargs={'pk': self.pk})


class City(models.Model):
    name = models.CharField(max_length=80)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return u'{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('city', kwargs={'pk': self.pk})