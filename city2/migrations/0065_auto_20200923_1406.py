# Generated by Django 3.0.2 on 2020-09-23 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city2', '0064_auto_20200923_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aslog',
            name='reporter',
            field=models.CharField(max_length=128, verbose_name='신고자'),
        ),
    ]
