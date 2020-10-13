# Generated by Django 3.0.2 on 2020-09-01 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city2', '0059_auto_20200901_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='aslog',
            name='as_worker',
            field=models.CharField(default='Suhdol', max_length=64, verbose_name='현장 조치자'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aslog',
            name='as_date',
            field=models.DateField(verbose_name='현장 조치일'),
        ),
    ]
