# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0004_auto_20151122_0224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journey',
            old_name='Event',
            new_name='event',
        ),
        migrations.AddField(
            model_name='flight',
            name='convey',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cartrip',
            name='drop',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 3, 25, 0, 559943), blank=True),
        ),
        migrations.AlterField(
            model_name='cartrip',
            name='pickup',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 3, 25, 0, 559885), blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 3, 25, 0, 561977), blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 3, 25, 0, 558403), blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 3, 25, 0, 558331), blank=True),
        ),
    ]
