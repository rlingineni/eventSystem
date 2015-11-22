# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0006_auto_20151122_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='convey',
            field=models.IntegerField(default=0, choices=[(0, b'No New Message'), (1, b'Message Due')]),
        ),
        migrations.AlterField(
            model_name='flight',
            name='journey',
            field=models.ForeignKey(default=0, to='ems.Journey'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, b'Default'), (1, b'OnTime'), (2, b'Landed'), (3, b'Delay'), (4, b'Cancelled')]),
        ),
    ]
