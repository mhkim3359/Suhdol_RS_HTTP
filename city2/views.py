from django.shortcuts import render
from django.views.generic import ListView, DetailView
from city2.models import City, Intersection, ASLog, Dust

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from mysite.views import OwnerOnlyMixin
from city2.forms import CityInlineFormSet
from django.db import IntegrityError        # 2020-05-27 by fantasy8 (교차로 명 중복 오류 체크)
from datetime import datetime

# Create your views here.

class CityLV(ListView):
    model = City

class CityDV(DetailView):
    model = City

class IntersectionDV(DetailView):
    model = Intersection


# Create/Change-List/Update/Delete
class IntersectionAddCV(LoginRequiredMixin, CreateView):
    model = Intersection
    fields = ('int_id', 'model_name', 'man_company', 'make_date', 'cpu_version', 'cpu_bd_kind', 'case_status',
        'bd_ins_kind', 'latitude', 'longitude', 'orientation', 'latitude2', 'longitude2', 'orientation2', 'image', 
        'image2', 'int_name', 'description', 'product_type')
    success_url = reverse_lazy('city:index')

    def form_valid(self, form):
        try :
            form.instance.owner = self.request.user
            return super().form_valid(form)
        except IntegrityError as e:
            messagebox.showinfo(title="DB 중복 에러", message="교차로 이름이 중복되었습니다.")

class IntersectionChangeLV(LoginRequiredMixin, ListView):
    model = Intersection
    template_name = 'city2/intersection_change_list.html'

    def get_queryset(self):
        return Intersection.objects.filter(owner=self.request.user)

class IntersectionUpdateUV(OwnerOnlyMixin, UpdateView):
    model = Intersection
    fields = ('int_id', 'model_name', 'man_company', 'make_date', 'cpu_version', 'cpu_bd_kind', 'case_status',
        'bd_ins_kind', 'latitude', 'longitude', 'orientation', 'latitude2', 'longitude2', 'orientation2',
        'image', 'image2', 'int_name', 'description', 'product_type')
    success_url = reverse_lazy('city:intersection_change')

class IntersectionDeleteV(OwnerOnlyMixin, DeleteView):
    model = Intersection
    success_url = reverse_lazy('city:intersection_change')

# 통계 데이터 처리를 위한 교차로 정보 목록 추출 (계정 체크는 없음)
class IntersectionLVStat(ListView):
    model = City
    template_name = 'city2/intersection_statistics.html'

class CityChangeLV(LoginRequiredMixin, ListView):
    model = City
    template_name = 'city2/city_change_list.html'

    def get_queryset(self):
        return City.objects.filter(owner=self.request.user)

class CityDeleteV(OwnerOnlyMixin, DeleteView):
    model = City
    success_url = reverse_lazy('city:city_change')

class CityAddCV(LoginRequiredMixin, CreateView):
    model = City
    fields = ['city_name', 'latitude', 'longitude', 'zoom', 'description']
    success_url = reverse_lazy('city:index')

    def form_valid(self, form):
        try :
            form.instance.owner = self.request.user
            return super().form_valid(form)
        except IntegrityError as e:
            messagebox.showinfo(title="DB 중복 에러", message="교차로 이름이 중복되었습니다.")

class CityUpdateUV(LoginRequiredMixin, UpdateView):
    model = City
    fields = ('city_name', 'latitude', 'longitude', 'zoom', 'description')
    success_url = reverse_lazy('city:index')


# A/S 이력 관련 함수들
# 2020-09-01 : as_date, as_worker 필드 추가
# 2020-09-02 : 삭제 관련 함수들 추가(이력 정보 삭제 기능의 필요성)
# 2020-09-23 : 신고자(reporter) 추가
class ASLogAddCV(LoginRequiredMixin, CreateView):
    model = ASLog
    template_name = 'city2/aslog_form.html'
    fields = ('city_no', 'int_no', 'title', 'reporter', 'as_date', 'as_worker', 'description', 'detail_info')
    success_url = reverse_lazy('city:index')    

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ASLogUpdateUV(OwnerOnlyMixin, UpdateView):
    model = ASLog
    fields = ('city_no', 'int_no', 'title', 'reporter', 'as_date', 'as_worker', 'description', 'detail_info')
    success_url = reverse_lazy('city:aslog_change')

class ASLogDeleteV(OwnerOnlyMixin, DeleteView):
    model = ASLog
    success_url = reverse_lazy('city:aslog_change')

class ASLogChangeLV(LoginRequiredMixin, ListView):
    model = ASLog
    template_name = 'city2/aslog_change_list.html'

    def get_queryset(self):
        return ASLog.objects.filter(owner=self.request.user)

class ASLogLV(ListView):
    model = ASLog
    template_name = 'city2/aslog_list.html'

class ASLogDetailLV(ListView):
    model = ASLog
    template_name = 'city2/aslog_detail_list.html'


# 미세먼지 로그 처리 관련 함수들
class DustLogLV(ListView):
    model = Dust
    template_name = 'city2/dustlog_list.html'

# 시간대별 미세먼지 측정 결과 처리
# 템플릿 파일에서는 별칭(date, pm10, pm25, pm100) 정보를 사용
class DustLogHourLV(ListView):
  template_name = 'city2/dustlog_hour_list.html'

  def get_queryset(self):
    return Dust.objects.raw("SELECT id, \
      DATE_FORMAT(log_datetime, '%%Y-%%m-%%d %%H') AS date, avg(pm_1_0) AS pm10, avg(pm_2_5) AS pm25, avg(pm_10_0) AS pm100 \
        FROM city2_dust GROUP BY DATE_FORMAT(log_datetime, '%%Y-%%m-%%d %%H') ORDER BY date DESC")

# 일별 미세먼지 측정 결과 처리
# 템플릿 파일에서는 별칭(date, pm10, pm25, pm100) 정보를 사용
class DustLogDayLV(ListView):
  template_name = 'city2/dustlog_day_list.html'

  def get_queryset(self):
    return Dust.objects.raw("SELECT id, \
      DATE_FORMAT(log_datetime, '%%Y-%%m-%%d') AS date, avg(pm_1_0) AS pm10, avg(pm_2_5) AS pm25, avg(pm_10_0) AS pm100 \
        FROM city2_dust GROUP BY DATE_FORMAT(log_datetime, '%%Y-%%m-%%d') ORDER BY date DESC")

