# Generated by Django 2.2.2 on 2019-06-15 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0004_auto_20190612_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traningword',
            name='name',
        ),
        migrations.RemoveField(
            model_name='traningword',
            name='slug',
        ),
    ]
