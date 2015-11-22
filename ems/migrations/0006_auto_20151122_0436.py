# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0005_auto_20151122_0325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='car',
        ),
        migrations.RemoveField(
            model_name='journey',
            name='flight',
        ),
        migrations.AddField(
            model_name='flight',
            name='journey',
            field=models.ForeignKey(default=0, choices=[(0, b'Default'), (1, b'OnTime'), (2, b'Landed'), (3, b'Delay'), (4, b'Cancelled')], to='ems.Journey'),
        ),
        migrations.AlterField(
            model_name='cartrip',
            name='drop',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
        ),
        migrations.AlterField(
            model_name='cartrip',
            name='pickup',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
        ),
    ]
