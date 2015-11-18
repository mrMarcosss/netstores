from django.db import models


class Person(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_VAR = (
        (GENDER_MALE, u'male'),
        (GENDER_FEMALE, u'female'),
    )

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    gender = models.SmallIntegerField(choices=GENDER_VAR)
    birth_date = models.DateField(blank=True, null=True)
    email = models.EmailField(unique=True)

    def __unicode__(self):
        return u'{} {}'.format(self.first_name, self.last_name)
