# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0002_auto_20151121_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='flight',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='journey',
            name='Event',
            field=models.ForeignKey(default=1, to='ems.Event'),
        ),
    ]
