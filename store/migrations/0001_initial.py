# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
        ('storage', '0001_initial'),
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=250)),
                ('site', models.URLField(null=True, blank=True)),
                ('city', models.ForeignKey(to='place.City')),
                ('owner', models.ForeignKey(related_name='own_store', to='person.Person')),
                ('sellers', models.ForeignKey(related_name='seller_in', to='person.Person')),
                ('storage', models.ForeignKey(to='storage.Storage')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfStore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='type',
            field=models.ForeignKey(to='store.TypeOfStore'),
        ),
    ]
