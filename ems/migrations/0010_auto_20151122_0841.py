# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0009_auto_20151122_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartrip',
            name='journey',
            field=models.ForeignKey(to='ems.Journey'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile_number',
            field=models.CharField(max_length=20, verbose_name=b'Phone Number'),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, b'Default'), (1, b'OnTime'), (2, b'Cancelled'), (3, b'Delay')]),
        ),
    ]
