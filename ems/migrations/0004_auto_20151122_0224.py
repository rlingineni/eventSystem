# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0003_auto_20151122_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartrip',
            name='drop',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 2, 24, 2, 968745), blank=True),
        ),
        migrations.AlterField(
            model_name='cartrip',
            name='num_of_cars',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cartrip',
            name='pickup',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 2, 24, 2, 968705), blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 2, 24, 2, 970145), blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 2, 24, 2, 967863), blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 2, 24, 2, 967826), blank=True),
        ),
    ]
