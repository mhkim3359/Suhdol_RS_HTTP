# Generated by Django 3.0.2 on 2020-03-24 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city2', '0008_intersection_man_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intersection',
            name='man_company',
            field=models.CharField(choices=[('서돌전자통신', '서돌전자통신'), ('코스텍', '코스텍'), ('세인시스템', '세인시스템'), ('엘케이일레븐', '엘케이일레븐'), ('진우산전', '진우산전'), ('진우전자', '진우전자'), ('기타', '기타')], max_length=64, verbose_name='제조사'),
        ),
    ]