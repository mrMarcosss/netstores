# coding=utf-8
from django.db import models
from place.models import City


class Storage(models.Model):
    name = models.CharField(max_length=80)
    city = models.ForeignKey(City)
    address = models.CharField(max_length=100)

    def __unicode__(self):
        return u'{}'.format(self.name)
