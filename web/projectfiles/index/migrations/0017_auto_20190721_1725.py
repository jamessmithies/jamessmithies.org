# Generated by Django 2.2 on 2019-07-21 17:25

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_presentations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='about',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='About'),
        ),
        migrations.AlterField(
            model_name='credits',
            name='about',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='About'),
        ),
        migrations.AlterField(
            model_name='credits',
            name='slug',
            field=models.SlugField(help_text='Suggested value automatically generated from title. Must be unique.', max_length=100, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='design',
            name='about',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='About'),
        ),
        migrations.AlterField(
            model_name='design',
            name='slug',
            field=models.SlugField(help_text='Suggested value automatically generated from title. Must be unique.', max_length=100, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='influences',
            name='about',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='About'),
        ),
        migrations.AlterField(
            model_name='presentations',
            name='about',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='About'),
        ),
        migrations.AlterField(
            model_name='presentations',
            name='slug',
            field=models.SlugField(help_text='Suggested value automatically generated from title. Must be unique.', max_length=100, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='writing',
            name='about',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='About'),
        ),
        migrations.AlterField(
            model_name='writing',
            name='slug',
            field=models.SlugField(help_text='Suggested value automatically generated from title. Must be unique.', max_length=100, unique=True, verbose_name='Slug'),
        ),
    ]
