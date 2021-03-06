# Generated by Django 3.0.2 on 2020-04-27 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('city2', '0010_auto_20200427_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='ASLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='타이틀')),
                ('slug', models.SlugField(allow_unicode=True, help_text='별칭용 하나의 단어(고유한 정보)', unique=True, verbose_name='SLUG')),
                ('description', models.CharField(blank=True, help_text='A/S 관련 간단한 한 줄 설명', max_length=100, verbose_name='설명')),
                ('content', models.TextField(verbose_name='세부 정보')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('modify_dt', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('int_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city2.Intersection')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='OWNER')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'aslog',
                'verbose_name_plural': 'aslogs',
                'ordering': ('-modify_dt',),
            },
        ),
    ]
