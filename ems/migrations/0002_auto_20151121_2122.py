# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarTrip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=20)),
                ('pickup', models.DateTimeField()),
                ('drop', models.DateTimeField()),
                ('type', models.CharField(max_length=20)),
                ('confirmation_no', models.CharField(max_length=20)),
                ('num_of_cars', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('mobile_number', models.IntegerField(verbose_name=b'Phone Number')),
                ('trip_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('airline', models.CharField(max_length=10)),
                ('departure', models.DateTimeField()),
                ('arrival', models.DateTimeField()),
                ('reference_no', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('car', models.ForeignKey(to='ems.CarTrip')),
                ('customer', models.ForeignKey(to='ems.Customer')),
                ('flight', models.ForeignKey(to='ems.Flight')),
            ],
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
