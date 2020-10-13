# Generated by Django 3.0.2 on 2020-08-14 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city2', '0057_auto_20200728_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intersection',
            name='man_company',
            field=models.CharField(choices=[('서돌전자통신', '서돌전자통신'), ('코스텍', '코스텍'), ('세인시스템', '세인시스템'), ('엘케이일레븐', '엘케이일레븐'), ('한국전기교통', '한국전기교통'), ('진우산전', '진우산전'), ('(주)신호', '(주)신호'), ('진우전자', '진우전자'), ('양광', '양광'), ('엘티시스템(LTS)', '엘티시스템(LTS)'), ('옵토피아', '옵토피아'), ('포에프', '포에프'), ('태경', '태경'), ('고엽제', '고엽제'), ('대한신호', '대한신호'), ('태림전자', '태림전자'), ('샤이니테크', '샤이니테크'), ('한진이엔씨', '한진이엔씨'), ('한길에이치씨', '한길에이치씨'), ('에스에이텍', '에스에이텍'), ('모루시스템', '모루시스템'), ('명신엔지니어링', '명신엔지니어링'), ('우리시스템', '우리시스템'), ('삼성SDS', '삼성SDS'), ('대진ENC', '대진ENC'), ('대진TNS', '대진TNS'), ('대성신호', '대성신호'), ('태양신호시스템', '태양신호시스템'), ('삼일신호공사', '삼일신호공사'), ('인터라이텍', '인터라이텍'), ('와이케이테크', '와이케이테크'), ('영인글로벌', '영인글로벌'), ('일렉시스테크놀러지', '일렉시스테크놀러지'), ('태은', '태은'), ('명서산업', '명서산업'), ('일도산업', '일도산업'), ('KC전자', 'KC전자'), ('위훈용사복지회', '위훈용사복지회'), ('한국노인생활지원재단', '한국노인생활지원재단'), ('기타', '기타')], max_length=64, verbose_name='제조사'),
        ),
        migrations.AlterField(
            model_name='intersection',
            name='model_name',
            field=models.CharField(choices=[('SEC-9000', 'SEC-9000'), ('SEC-N9000', 'SEC-N9000'), ('SEC-N9400', 'SEC-N9400'), ('SEC-S9400', 'SEC-S9400'), ('SEC-N9500', 'SEC-N9500'), ('SEC-P9600', 'SEC-P9600'), ('COEL-TSC100', 'COEL-TSC100'), ('COEL-TSC200', 'COEL-TSC200'), ('COEL-TS-500', 'COEL-TS-500'), ('COEL-TSC1000', 'COEL-TSC1000'), ('CJH-1000', 'CJH-1000'), ('CTSC-3000', 'CTSC-3000'), ('CTSC-3000-BS', 'CTSC-3000-BS'), ('DBLC-S2', 'DBLC-S2'), ('DJ-7000', 'DJ-7000'), ('DS-1000', 'DS-1000'), ('DS-2000', 'DS-2000'), ('EST-5000A', 'EST-5000A'), ('GSC-A1', 'GSC-A1'), ('GTL-TSC100', 'GTL-TSC100'), ('HJ-5000', 'HJ-5000'), ('HJ-5000H', 'HJ-5000H'), ('HJ-5000T', 'HJ-5000T'), ('HTC-7100A', 'HTC-7100A'), ('ILT-TSC-100S', 'ILT-TSC-100S'), ('IT-1600', 'IT-1600'), ('JM-100', 'JM-100'), ('JW-7000', 'JW-7000'), ('JW-7000A', 'JW-7000A'), ('JW-7000-S', 'JW-7000-S'), ('JWS-7000-S', 'JWS-7000-S'), ('JWI-8000', 'JWI-8000'), ('JWIS-8000', 'JWIS-8000'), ('JWIS-9600', 'JWIS-9600'), ('JWTC-LC-G01', 'JWTC-LC-G01'), ('KCL-5000A', 'KCL-5000A'), ('KES-7000', 'KES-7000'), ('KESAD-3100', 'KESAD-3100'), ('KET-2100', 'KET-2100'), ('KET-2100N', 'KET-2100N'), ('KET-3100MA', 'KET-3100MA'), ('KET-3100SB', 'KET-3100SB'), ('KAOVA-STC', 'KAOVA-STC'), ('KSC-2800', 'KSC-2800'), ('KSC-2800S', 'KSC-2800S'), ('KSC-5800S', 'KSC-5800S'), ('KSC-5800SE', 'KSC-5800SE'), ('LK-3100', 'LK-3100'), ('LK-4000', 'LK-4000'), ('LTK-2000', 'LTK-2000'), ('MIT-9000S', 'MIT-9000S'), ('MS-A2000', 'MS-A2000'), ('NI-2000', 'NI-2000'), ('OPT-5000', 'OPT-5000'), ('OPT-9000A', 'OPT-9000A'), ('OPT-9200S', 'OPT-9200S'), ('OT-2000', 'OT-2000'), ('PS-9000', 'PS-2000'), ('Road-5000', 'Road-5000'), ('SH-B2000', 'SH-B2000'), ('SDS-9000', 'SDS-9000'), ('SDS-9000A', 'SDS-9000A'), ('SDS-9000B', 'SDS-9000B'), ('SDS-9000S', 'SDS-9000S'), ('SJS-2000', 'SJS-2000'), ('SJS-3000', 'SJS-3000'), ('SLC-S2000', 'SLC-S2000'), ('SLC-S2000-(A)', 'SLC-S2000-(A)'), ('SLC-S3000', 'SLC-S3000'), ('SLC-S5000', 'SLC-S5000'), ('SMS-5000', 'SMS-5000'), ('SMS-5000-SB', 'SMS-5000-SB'), ('ST-09SL', 'ST-09SL'), ('ST-09ST-D', 'ST-09ST-D'), ('STC-3000', 'STC-3000'), ('STCM-SBB4', 'STCM-SBB4'), ('STE-8000', 'STE-8000'), ('STLC-S01', 'STLC-S01'), ('STLC-S2', 'STLC-S2'), ('STLC-S2-(2)', 'STLC-S2-(2)'), ('STLC-S3', 'STLC-S3'), ('STS045', 'STS045'), ('STS-046', 'STS-046'), ('TC-9000A', 'TC-9000A'), ('TG-7000S', 'TG-7000S'), ('TG-7000SS', 'TG-7000SS'), ('TYS-1000', 'TYS-1000'), ('UKET-2100', 'UKET-2100'), ('UKET-3100SB', 'UKET-3100SB'), ('WH-100', 'WH-100'), ('WS-2300', 'WS-2300'), ('Y-6000', 'Y-6000'), ('Y-6000A', 'Y-6000A'), ('Y-8000', 'Y-8000'), ('Y-8000A', 'Y-8000A'), ('YG-5000', 'YG-5000'), ('YK-5000', 'YK-5000'), ('YK-6000', 'YK-6000'), ('YK-6000B', 'YK-6000B'), ('ZEO-TSC-601', 'ZEO-TSC-601'), ('기타', '기타')], max_length=64, verbose_name='모델명'),
        ),
    ]
