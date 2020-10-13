# Generated by Django 3.0.2 on 2020-06-09 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city2', '0036_auto_20200609_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intersection',
            name='man_company',
            field=models.CharField(choices=[('서돌전자통신', '서돌전자통신'), ('코스텍', '코스텍'), ('세인시스템', '세인시스템'), ('엘케이일레븐', '엘케이일레븐'), ('한국전기교통', '한국전기교통'), ('진우산전', '진우산전'), ('(주)신호', '(주)신호'), ('진우전자', '진우전자'), ('양광', '양광'), ('옵토피아', '옵토피아'), ('포에프', '포에프'), ('태경', '태경'), ('고엽제', '고엽제'), ('대한신호', '대한신호'), ('태림전자', '태림전자'), ('샤이니테크', '샤이니테크'), ('한진이엔씨', '한진이엔씨'), ('한길에이치씨', '한길에이치씨'), ('에스에이텍', '에스에이텍'), ('대진ENC', '대진ENC'), ('기타', '기타')], max_length=64, verbose_name='제조사'),
        ),
        migrations.AlterField(
            model_name='intersection',
            name='model_name',
            field=models.CharField(choices=[('SEC-N9400', 'SEC-N9400'), ('SEC-N9500', 'SEC-N9500'), ('SEC-P9600', 'SEC-P9600'), ('COEL-TSC100', 'COEL-TSC100'), ('CJH-1000', 'CJH-1000'), ('CTSC-3000', 'CTSC-3000'), ('CTSC-3000-BS', 'CTSC-3000-BS'), ('DJ-7000', 'DJ-7000'), ('HJ-5000H', 'HJ-5000H'), ('HTC-7100A', 'HTC-7100A'), ('JW-7000', 'JW-7000'), ('JW-7000A', 'JW-7000A'), ('JW-7000-S', 'JW-7000-S'), ('JWS-7000-S', 'JWS-7000-S'), ('JWTC-LC-G01', 'JWTC-LC-G01'), ('KET-2100', 'KET-2100'), ('KAOVA-STC', 'KAOVA-STC'), ('KSC-5800SE', 'KSC-5800SE'), ('MIT-9000S', 'MIT-9000S'), ('NI-2000', 'NI-2000'), ('OPT-9000A', 'OPT-9000A'), ('OPT-9200S', 'OPT-9200S'), ('OT-2000', 'OT-2000'), ('Road-5000', 'Road-5000'), ('SDS-9000', 'SDS-9000'), ('SDS-9000A', 'SDS-9000A'), ('SDS-9000B', 'SDS-9000B'), ('SDS-9000S', 'SDS-9000S'), ('SJS-2000', 'SJS-2000'), ('SJS-3000', 'SJS-3000'), ('ST-09ST-D', 'ST-09ST-D'), ('STLC-S01', 'STLC-S01'), ('STLC-S3', 'STLC-S3'), ('TC-9000A', 'TC-9000A'), ('TG-7000S', 'TG-7000S'), ('UKET-2100', 'UKET-2100'), ('UKET-3100SB', 'UKET-3100SB'), ('Y-6000', 'Y-6000'), ('YK-6000', 'YK-6000'), ('기타', '기타')], max_length=64, verbose_name='모델명'),
        ),
    ]
