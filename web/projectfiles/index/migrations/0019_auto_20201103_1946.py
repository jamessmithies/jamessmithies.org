# Generated by Django 2.2.13 on 2020-11-03 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0018_auto_20190727_1851'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Outputs',
            new_name='Writing',
        ),
        migrations.AlterModelOptions(
            name='writing',
            options={'verbose_name_plural': 'Writing'},
        ),
    ]