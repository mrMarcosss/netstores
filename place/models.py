# coding=utf-8
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __unicode__(self):
        return u'{}'.format(self.name)
