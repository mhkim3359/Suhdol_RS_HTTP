# Generated by Django 3.0.2 on 2020-05-26 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city2', '0024_auto_20200526_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intersection',
            name='int_name',
            field=models.CharField(max_length=64, verbose_name='교차로명'),
        ),
    ]
