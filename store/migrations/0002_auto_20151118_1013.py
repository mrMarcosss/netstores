# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
        ('person', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='sellers',
        ),
        migrations.AddField(
            model_name='store',
            name='sellers',
            field=models.ManyToManyField(related_name='seller_in', to='person.Person'),
        ),
        migrations.RemoveField(
            model_name='store',
            name='storage',
        ),
        migrations.AddField(
            model_name='store',
            name='storage',
            field=models.ManyToManyField(to='storage.Storage'),
        ),
    ]
