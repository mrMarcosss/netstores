# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20151118_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='v',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
