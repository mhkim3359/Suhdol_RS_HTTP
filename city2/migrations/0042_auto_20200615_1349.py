# Generated by Django 3.0.2 on 2020-06-15 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city2', '0041_auto_20200615_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='zoom',
            field=models.IntegerField(default=11, verbose_name='Zoom'),
        ),
    ]
