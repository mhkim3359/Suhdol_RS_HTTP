from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager 
from django.utils.text import slugify

from city2.fields import ThumbnailImageField

# Create your models here.

class City(models.Model):
    city_name = models.CharField('도시명', max_length=128, unique=True)
    latitude = models.FloatField('GPS 위도')
    longitude = models.FloatField('GPS 경도')
    zoom = models.IntegerField('Zoom', default=11)
    description = models.CharField('기타 설명', max_length=100, blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

    class Meta:
        ordering = ('city_name', )

    def __str__(self):
        return self.city_name

    def get_absolute_url(self):
        return reverse('city:city_detail', args=(self.id,))

class Intersection(models.Model):
    MODEL_CHOICES = (
        ('SEC-9000', 'SEC-9000'),
        ('SEC-9400', 'SEC-9400'),
        ('SEC-N9000', 'SEC-N9000'),
		    ('SEC-N9400', 'SEC-N9400'),
        ('SEC-S9400', 'SEC-S9400'),
        ('SEC-N9500', 'SEC-N9500'),
        ('SEC-P9600', 'SEC-P9600'),
        ('COEL-TSC100', 'COEL-TSC100'),
        ('COEL-TSC200', 'COEL-TSC200'),
        ('COEL-TS-500', 'COEL-TS-500'),
        ('COEL-TSC1000', 'COEL-TSC1000'),
        ('CJH-1000', 'CJH-1000'),
        ('CTSC-3000', 'CTSC-3000'),
        ('CTSC-3000-BS', 'CTSC-3000-BS'),
        ('CTSC-STD', 'CTSC-STD'),
        ('DBLC-S2', 'DBLC-S2'),
        ('DJ-7000', 'DJ-7000'),
        ('DS-1000', 'DS-1000'),
        ('DS-2000', 'DS-2000'),
        ('EST-5000A', 'EST-5000A'),
        ('GSC-A1', 'GSC-A1'),
        ('GTL-TSC100', 'GTL-TSC100'),
        ('HJ-5000', 'HJ-5000'),
        ('HJ-5000H', 'HJ-5000H'),
        ('HJ-5000T', 'HJ-5000T'),
        ('HTC-7100A', 'HTC-7100A'),
        ('ILT-TSC-100S', 'ILT-TSC-100S'),
        ('IT-1600', 'IT-1600'),
        ('JM-100', 'JM-100'),
        ('JW-7000', 'JW-7000'),
        ('JW-7000A', 'JW-7000A'),
        ('JW-7000-S', 'JW-7000-S'),
        ('JWS-7000-S', 'JWS-7000-S'),
        ('JWI-8000', 'JWI-8000'),
        ('JWIS-8000', 'JWIS-8000'),
        ('JWIS-9600', 'JWIS-9600'),
        ('JWTC-LC-G01', 'JWTC-LC-G01'),
        ('KCL-5000A', 'KCL-5000A'),
        ('KES-7000', 'KES-7000'),
        ('KESAD-3100', 'KESAD-3100'),
        ('KET-2100', 'KET-2100'),
        ('KET-2100N', 'KET-2100N'),
        ('KET-3100MA', 'KET-3100MA'),
        ('KET-3100SB', 'KET-3100SB'),
        ('KAOVA-STC', 'KAOVA-STC'),
        ('KSC-2800', 'KSC-2800'),
        ('KSC-2800S', 'KSC-2800S'),
        ('KSC-5800S', 'KSC-5800S'),
        ('KSC-5800SE', 'KSC-5800SE'),
        ('LK-3100', 'LK-3100'),
        ('LK-4000', 'LK-4000'),
        ('LTK-2000', 'LTK-2000'),
        ('MIT-9000S', 'MIT-9000S'),
        ('MS-A2000', 'MS-A2000'),
        ('NI-2000', 'NI-2000'),
        ('OPT-5000', 'OPT-5000'),
        ('OPT-9000A', 'OPT-9000A'),
        ('OPT-9200S', 'OPT-9200S'),
        ('OT-2000', 'OT-2000'),
        ('PS-9000', 'PS-2000'),
        ('Road-5000', 'Road-5000'),
        ('SH-B2000', 'SH-B2000'),
        ('SDS-9000', 'SDS-9000'),
        ('SDS-9000A', 'SDS-9000A'),
        ('SDS-9000B', 'SDS-9000B'),
        ('SDS-9000S', 'SDS-9000S'),
        ('SJ-3000', 'SJ-3000'),
        ('SJ-5000', 'SJ-5000'),
        ('SJS-2000', 'SJS-2000'),
        ('SJS-3000', 'SJS-3000'),
        ('SLC-S1000', 'SLC-S1000'),
        ('SLC-S2000', 'SLC-S2000'),
        ('SLC-S2000-(A)', 'SLC-S2000-(A)'),
        ('SLC-S3000', 'SLC-S3000'),
        ('SLC-S5000', 'SLC-S5000'),
        ('SLC-S9000', 'SLC-S9000'),
        ('SMS-5000', 'SMS-5000'),
        ('SMS-5000-SB', 'SMS-5000-SB'),
        ('ST-09SL', 'ST-09SL'),
        ('ST-09ST-D', 'ST-09ST-D'),
        ('STC-3000', 'STC-3000'),
        ('STCM-SBB4', 'STCM-SBB4'),
        ('STE-8000', 'STE-8000'),
        ('STLC-S01', 'STLC-S01'),
        ('STLC-S2', 'STLC-S2'),
        ('STLC-S2-(2)', 'STLC-S2-(2)'),
        ('STLC-S3', 'STLC-S3'),
        ('STS045', 'STS045'),
        ('STS-046', 'STS-046'),
        ('TC-9000A', 'TC-9000A'),
        ('TG-7000S', 'TG-7000S'),
        ('TG-7000SS', 'TG-7000SS'),
        ('TKSTDLC-1000', 'TKSTDLC-1000'),
        ('TYS-1000', 'TYS-1000'),
        ('UKET-2100', 'UKET-2100'),
        ('UKET-3100SB', 'UKET-3100SB'),
        ('VS21-9000', 'VS21-9000'),
        ('WH-100', 'WH-100'),
        ('WRLC-S100', 'WRLC-S100'),
        ('WRLC-S1000', 'WRLC-S1000'),
        ('WS-2300', 'WS-2300'),
        ('Y-6000', 'Y-6000'),
        ('Y-6000A', 'Y-6000A'),
        ('Y-8000', 'Y-8000'),
        ('Y-8000A', 'Y-8000A'),
        ('YG-5000', 'YG-5000'),
        ('YK-3000', 'YK-3000'),
        ('YK-5000', 'YK-5000'),
        ('YK-6000', 'YK-6000'),
        ('YK-6000B', 'YK-6000B'),
        ('ZEO-TSC-601', 'ZEO-TSC-601'),
        ('기타', '기타'),
    )

    CPU_BOARD_CHOICES = (
		('2450', '2450'),
        ('386', '386'),
        ('신형', '신형'),
        ('기타', '기타'),
    )

    MANUFACTURE_COMPANY = (
		('서돌전자통신', '서돌전자통신'),
        ('코스텍', '코스텍'),
        ('세인시스템', '세인시스템'),
        ('엘케이일레븐', '엘케이일레븐'),
        ('한국전기교통', '한국전기교통'),
        ('진우산전', '진우산전'),
        ('(주)신호', '(주)신호'),
        ('진우전자', '진우전자'),
        ('양광', '양광'),
        ('엘티시스템(LTS)', '엘티시스템(LTS)'),
        ('옵토피아', '옵토피아'),
        ('포에프', '포에프'),
        ('태경', '태경'),
        ('대한신호', '대한신호'),
        ('태림전자', '태림전자'),
        ('샤이니테크', '샤이니테크'),
        ('한진이엔씨', '한진이엔씨'),
        ('한길에이치씨', '한길에이치씨'),
        ('에스에이텍', '에스에이텍'),
        ('모루시스템', '모루시스템'),
        ('명신엔지니어링', '명신엔지니어링'),
        ('우리시스템', '우리시스템'),
        ('삼성SDS', '삼성SDS'),
        ('대진ENC', '대진ENC'),
        ('대진TNS', '대진TNS'),
        ('대성신호', '대성신호'),
        ('비젼21이앤씨', '비젼21이앤씨'),
        ('태양신호시스템', '태양신호시스템'),
        ('삼일신호공사', '삼일신호공사'),
        ('인터라이텍', '인터라이텍'),
        ('와이케이테크', '와이케이테크'),
        ('영인글로벌', '영인글로벌'),
        ('일렉시스테크놀러지', '일렉시스테크놀러지'),
        ('태은', '태은'),
        ('명서산업', '명서산업'),
        ('일도산업', '일도산업'),
        ('KC전자', 'KC전자'),
        ('위훈용사복지회', '위훈용사복지회'),
        ('한국노인생활지원재단', '한국노인생활지원재단'),
        ('기타', '기타'),
    )

    PRODUCT_TYPE = (
        ('교통신호제어기', '교통신호제어기'),
        ('영상검지기', '영상검지기'),
        ('루프검지기', '루프검지기'),
        ('보행자작동신호기', '보행자작동신호기'),
    )

    int_id = models.ForeignKey(City, on_delete=models.CASCADE)
    int_name = models.CharField('교차로명', max_length=128, unique=True)
    model_name = models.CharField('모델명', max_length=64, choices=MODEL_CHOICES)
    man_company = models.CharField('제조사', max_length=64, choices=MANUFACTURE_COMPANY)
    make_date	= models.DateField('제조년월일')
    cpu_version = models.CharField('CPU 버전', max_length=32)
    cpu_bd_kind = models.CharField('CPU 보드 종류', max_length=32, choices=CPU_BOARD_CHOICES)
    case_status = models.CharField('외관 상태', max_length=64)
    bd_ins_kind = models.CharField('보드 실장 상태', max_length=64)
    latitude = models.FloatField('GPS 위도')
    longitude = models.FloatField('GPS 경도')
    latitude2 = models.FloatField('GPS 위도(2)')
    longitude2 = models.FloatField('GPS 경도(2)')
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    image2 = ThumbnailImageField(upload_to='photo/%Y/%m')
    description = models.TextField('기타 정보', blank=True, help_text="추가로 기입하고자 하는 정보들 설정")
    orientation = models.IntegerField('사진 방향 정보', default=0)
    orientation2 = models.IntegerField('사진 방향 정보(2)', default=0)
    product_type = models.CharField('장비 타입', max_length=64, choices=PRODUCT_TYPE)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

    class Meta:
        ordering = ('int_name', )

    def __str__(self):
        return self.int_name

    def get_absolute_url(self):
        return reverse('city:intersection_detail', args=(self.id,))


# 현장 A/S 이력 로그 모델
# 2020-09-01 : 현장 조치 날짜 추가
# 2020-09-23 : 신고자(reporter) 추가
class ASLog(models.Model):
    city_no = models.ForeignKey(City, on_delete=models.CASCADE)
    int_no = models.ForeignKey(Intersection, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='증상', max_length=128)
    reporter = models.CharField(verbose_name='신고자', max_length=128)
    as_date	= models.DateField('작업일')
    as_worker	= models.CharField('작업자', max_length=64)
    description = models.CharField('조치', max_length=100, blank=True, help_text='A/S 관련 간단한 한 줄 설명')
    detail_info = models.TextField('세부 정보', max_length=300)
    create_dt = models.DateTimeField('생성일', auto_now_add=True)
    modify_dt = models.DateTimeField('수정일', auto_now=True)
    tags = TaggableManager(blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

    class Meta:
        verbose_name = 'aslog'
        verbose_name_plural = 'aslogs'
        ordering = ('-modify_dt', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('city:aslog_detail', args=(self.id,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)


class Dust(models.Model):
    log_datetime = models.DateTimeField('수집시점')
    pm_1_0 = models.IntegerField('PM 1.0')
    pm_2_5 = models.IntegerField('PM 2.5')
    pm_10_0 = models.IntegerField('PM 10.0')
    
    class Meta:
        ordering = ('log_datetime', )

    def __str__(self):
        return self.log_datetime
