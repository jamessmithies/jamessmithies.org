# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-16 19:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_library'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Library',
            new_name='Influences',
        ),
        migrations.AlterModelOptions(
            name='influences',
            options={'verbose_name_plural': 'Influences'},
        ),
    ]
