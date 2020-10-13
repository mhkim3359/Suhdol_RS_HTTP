# Generated by Django 3.0.2 on 2020-03-10 15:42

import city2.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=128, verbose_name='도시명')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='고양시/서울시 처럼 도시 이름')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='OWNER')),
            ],
            options={
                'ordering': ('city_name',),
            },
        ),
        migrations.CreateModel(
            name='Intersection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(choices=[('SEC-N9400', 'SEC-N9400'), ('SEC-N9500', 'SEC-N9500'), ('SEC-P9600', 'SEC-P9600')], max_length=64, verbose_name='모델명')),
                ('make_date', models.DateTimeField(verbose_name='제조년월일')),
                ('cpu_version', models.CharField(max_length=64, verbose_name='CPU 버전')),
                ('cpu_bd_kind', models.CharField(choices=[('2450', '2450'), ('386', '386'), ('신형', '신형')], max_length=32, verbose_name='CPU 보드 종류')),
                ('case_status', models.CharField(max_length=64, verbose_name='외관 상태')),
                ('bd_ins_kind', models.CharField(max_length=16, verbose_name='보드 실장 상태')),
                ('as_date', models.DateTimeField(verbose_name='기술 지원 날짜')),
                ('latitude', models.IntegerField(verbose_name='GPS 위도')),
                ('longitude', models.IntegerField(verbose_name='GPS 경도')),
                ('image', city2.fields.ThumbnailImageField(upload_to='photo/%Y/%m')),
                ('description', models.TextField(blank=True, verbose_name='사진 설명')),
                ('int_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city2.City')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='OWNER')),
            ],
            options={
                'ordering': ('int_name',),
            },
        ),
    ]
