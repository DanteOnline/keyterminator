# Generated by Django 2.2.2 on 2019-06-12 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_auto_20190612_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traningword',
            name='base_word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.Word'),
        ),
        migrations.AlterField(
            model_name='traningword',
            name='order_letters',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.OrderLetters'),
        ),
        migrations.AlterUniqueTogether(
            name='traningword',
            unique_together={('base_word', 'order_letters')},
        ),
    ]
