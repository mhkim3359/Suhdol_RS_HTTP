# Generated by Django 3.0.2 on 2020-05-06 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city2', '0019_auto_20200429_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intersection',
            name='as_date',
        ),
    ]
