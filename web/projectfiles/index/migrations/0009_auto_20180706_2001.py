# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-06 20:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_delete_cv'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='About',
            new_name='Bio',
        ),
        migrations.AlterModelOptions(
            name='bio',
            options={'verbose_name_plural': 'Bio'},
        ),
    ]
