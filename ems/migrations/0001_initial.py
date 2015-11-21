# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('airline', models.CharField(max_length=10)),
                ('departure', models.DateTimeField()),
                ('arrival', models.DateTimeField()),
            ],
        ),
    ]
