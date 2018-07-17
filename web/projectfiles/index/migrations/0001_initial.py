# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-19 19:22
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('displayName', models.CharField(blank=True, max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(help_text=b'Suggested value automatically generated from title. Must be unique.', max_length=100, unique=True, verbose_name=b'Slug')),
                ('about', ckeditor.fields.RichTextField(blank=True, verbose_name=b'About')),
            ],
            options={
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='cv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('displayName', models.CharField(blank=True, max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(help_text=b'Suggested value automatically generated from title. Must be unique.', max_length=100, unique=True, verbose_name=b'Slug')),
                ('content', ckeditor.fields.RichTextField(blank=True, verbose_name=b'Content')),
                ('version', models.CharField(blank=True, max_length=128)),
                ('datePublished', models.DateTimeField(blank=True, verbose_name=b'Date Published')),
                ('lastModified', models.DateTimeField(blank=True, verbose_name=b'Last Modified')),
            ],
            options={
                'verbose_name_plural': 'CV',
            },
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('displayName', models.CharField(blank=True, max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(help_text=b'Suggested value automatically generated from title. Must be unique.', max_length=100, unique=True, verbose_name=b'Slug')),
                ('about', ckeditor.fields.RichTextField(blank=True, verbose_name=b'About')),
                ('project1', ckeditor.fields.RichTextField(blank=True, verbose_name=b'Project1')),
                ('project2', ckeditor.fields.RichTextField(blank=True, verbose_name=b'Project2')),
                ('project3', ckeditor.fields.RichTextField(blank=True, verbose_name=b'Project3')),
                ('project4', ckeditor.fields.RichTextField(blank=True, verbose_name=b'Project4')),
                ('project5', ckeditor.fields.RichTextField(blank=True, verbose_name=b'Project5')),
                ('project6', ckeditor.fields.RichTextField(blank=True, verbose_name=b'Project6')),
                ('project7', ckeditor.fields.RichTextField(blank=True, verbose_name=b'Project7')),
                ('project8', ckeditor.fields.RichTextField(blank=True, verbose_name=b'Project8')),
                ('project9', ckeditor.fields.RichTextField(blank=True, verbose_name=b'Project9')),
                ('project10', ckeditor.fields.RichTextField(blank=True, verbose_name=b'Project10')),
                ('project11', ckeditor.fields.RichTextField(blank=True, verbose_name=b'Project11')),
                ('project12', ckeditor.fields.RichTextField(blank=True, verbose_name=b'Project12')),
            ],
            options={
                'verbose_name_plural': 'Laboratory Home',
            },
        ),
    ]
