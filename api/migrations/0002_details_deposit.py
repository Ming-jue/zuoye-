# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-02-10 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='deposit',
            field=models.PositiveIntegerField(default=1000, verbose_name='全场保证金'),
        ),
    ]
