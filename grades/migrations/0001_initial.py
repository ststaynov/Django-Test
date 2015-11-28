# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('grade_decimal', models.DecimalField(max_digits=2, decimal_places=1)),
                ('forecast_date', models.DateTimeField(verbose_name='date forecast')),
            ],
        ),
        migrations.CreateModel(
            name='Resort',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('resortname_text', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='grade',
            name='resort',
            field=models.ForeignKey(to='grades.Resort'),
        ),
    ]
