# Generated by Django 3.2.11 on 2022-04-15 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='user',
        ),
    ]
