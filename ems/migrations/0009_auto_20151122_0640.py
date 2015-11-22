# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0008_auto_20151122_0543'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartrip',
            name='journey',
            field=models.ForeignKey(default=0, to='ems.Journey'),
        ),
        migrations.AddField(
            model_name='event',
            name='convey',
            field=models.IntegerField(default=0, choices=[(0, b'Message Due'), (1, b'No New Message')]),
        ),
        migrations.AlterField(
            model_name='cartrip',
            name='num_of_cars',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='flight',
            name='journey',
            field=models.ForeignKey(to='ems.Journey'),
        ),
    ]
