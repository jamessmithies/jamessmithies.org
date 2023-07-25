# Generated by Django 3.2.16 on 2023-01-14 17:17

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0020_talks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(blank=True, max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(help_text='Suggested value automatically generated from title. Must be unique.', max_length=100, unique=True, verbose_name='Slug')),
                ('about', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='About')),
            ],
            options={
                'verbose_name_plural': 'Research',
            },
        ),
    ]
