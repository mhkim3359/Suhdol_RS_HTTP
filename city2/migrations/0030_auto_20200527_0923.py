# Generated by Django 3.0.2 on 2020-05-27 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city2', '0029_auto_20200527_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intersection',
            name='int_name',
            field=models.CharField(max_length=128, unique=True, verbose_name='교차로명'),
        ),
    ]