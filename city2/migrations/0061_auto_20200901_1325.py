# Generated by Django 3.0.2 on 2020-09-01 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city2', '0060_auto_20200901_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aslog',
            name='as_date',
            field=models.DateField(verbose_name='작업일'),
        ),
        migrations.AlterField(
            model_name='aslog',
            name='as_worker',
            field=models.CharField(max_length=64, verbose_name='작업자'),
        ),
    ]