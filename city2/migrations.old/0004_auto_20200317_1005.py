# Generated by Django 3.0.2 on 2020-03-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city2', '0003_auto_20200316_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intersection',
            name='latitude',
            field=models.FloatField(verbose_name='GPS 위도'),
        ),
        migrations.AlterField(
            model_name='intersection',
            name='longitude',
            field=models.FloatField(verbose_name='GPS 경도'),
        ),
    ]
