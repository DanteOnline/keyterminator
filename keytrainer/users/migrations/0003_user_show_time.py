# Generated by Django 2.2.2 on 2019-07-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190615_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='show_time',
            field=models.PositiveIntegerField(default=5),
        ),
    ]
