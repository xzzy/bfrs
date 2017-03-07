# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-07 05:31
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bfrs', '0004_remove_bushfire_arrival_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bushfire',
            name='fire_boundary',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, help_text=b'Optional.', null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='bushfire',
            name='origin_point',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, help_text=b'Optional.', null=True, srid=4326),
        ),
    ]
