from django.db import models
from person.models import Person
from place.models import City
from storage.models import Storage


class TypeOfStore(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'{}'.format(self.name)


class Store(models.Model):
    type = models.ForeignKey(TypeOfStore)
    name = models.CharField(max_length=80)
    owner = models.ForeignKey(Person, related_name='own_store')
    sellers = models.ManyToManyField(Person, related_name='seller_in')
    storage = models.ManyToManyField(Storage)
    city = models.ForeignKey(City)
    address = models.CharField(max_length=250)
    site = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return u'{} ({})'.format(self.name, self.type)
