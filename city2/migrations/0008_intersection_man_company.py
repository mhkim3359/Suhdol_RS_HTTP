# Generated by Django 3.0.2 on 2020-03-24 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city2', '0007_auto_20200320_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='intersection',
            name='man_company',
            field=models.CharField(choices=[('서돌전자통신', '서돌전자통신'), ('코스텍', '코스텍'), ('세인시스템', '세인시스템'), ('엘케이일레븐', '엘케이일레븐'), ('진우산전', '진우산전')], default=1, max_length=64, verbose_name='제조사'),
            preserve_default=False,
        ),
    ]
