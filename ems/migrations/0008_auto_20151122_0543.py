# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0007_auto_20151122_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='convey',
            field=models.IntegerField(default=0, choices=[(0, b'Message Due'), (1, b'No New Message')]),
        ),
    ]
