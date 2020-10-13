# Generated by Django 3.0.2 on 2020-04-27 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city2', '0009_auto_20200324_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intersection',
            name='cpu_bd_kind',
            field=models.CharField(choices=[('2450', '2450'), ('386', '386'), ('신형', '신형'), ('기타', '기타')], max_length=32, verbose_name='CPU 보드 종류'),
        ),
        migrations.AlterField(
            model_name='intersection',
            name='man_company',
            field=models.CharField(choices=[('서돌전자통신', '서돌전자통신'), ('코스텍', '코스텍'), ('세인시스템', '세인시스템'), ('엘케이일레븐', '엘케이일레븐'), ('한국전기교통', '한국전기교통'), ('진우산전', '진우산전'), ('진우전자', '진우전자'), ('기타', '기타')], max_length=64, verbose_name='제조사'),
        ),
        migrations.AlterField(
            model_name='intersection',
            name='model_name',
            field=models.CharField(choices=[('SEC-N9400', 'SEC-N9400'), ('SEC-N9500', 'SEC-N9500'), ('SEC-P9600', 'SEC-P9600'), ('CJH-1000', 'CJH-1000'), ('STLC-S01', 'STLC-S01'), ('SDS-9000', 'SDS-9000'), ('TC-9000A', 'TC-9000A'), ('기타', '기타')], max_length=64, verbose_name='모델명'),
        ),
    ]