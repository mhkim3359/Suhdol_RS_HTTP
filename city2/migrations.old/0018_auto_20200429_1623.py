# Generated by Django 3.0.2 on 2020-04-29 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city2', '0017_auto_20200429_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aslog',
            old_name='content',
            new_name='contents',
        ),
    ]