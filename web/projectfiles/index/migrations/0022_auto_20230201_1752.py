# Generated by Django 3.2.16 on 2023-02-01 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0021_research'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Talks',
        ),
        migrations.DeleteModel(
            name='Writing',
        ),
    ]