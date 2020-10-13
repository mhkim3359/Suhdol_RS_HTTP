# Generated by Django 3.0.2 on 2020-04-27 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city2', '0013_auto_20200427_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='intersection',
            name='product_type',
            field=models.CharField(choices=[('교통신호제어기', '교통신호제어기'), ('영상검지기', '영상검지기'), ('루프검지기', '루프검지기'), ('VDU(좌회전 감응)', 'VDU(좌회전 감응)')], default=1, max_length=64, verbose_name='장비 타입'),
            preserve_default=False,
        ),
    ]