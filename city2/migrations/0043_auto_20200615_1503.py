# Generated by Django 3.0.2 on 2020-06-15 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city2', '0042_auto_20200615_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city_name',
            field=models.CharField(max_length=128, unique=True, verbose_name='도시명'),
        ),
    ]