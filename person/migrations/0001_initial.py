# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('gender', models.SmallIntegerField(choices=[(0, 'male'), (1, 'female')])),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
            ],
        ),
    ]
