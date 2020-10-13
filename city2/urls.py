from django.urls import path
from city2 import views

app_name = 'city'
urlpatterns = [
    # /city/
    path('', views.CityLV.as_view(), name='index'),

    # /city/city/
    path('city/', views.CityLV.as_view(), name='city_list'),

    # /city/city/99/
    path('city/<int:pk>', views.CityDV.as_view(), name='city_detail'),

    # /city/intersection/99/
    path('intersection/<int:pk>', views.IntersectionDV.as_view(), name='intersection_detail'),

    # 등록/수정/삭제 관련 URL 처리
    # /city/city/add/
    path('city/add/', views.CityAddCV.as_view(), name='city_add', ),

    # /city/city/change/
    path('city/change/', views.CityChangeLV.as_view(), name='city_change', ),

    # /city/city/99/update/
    path('city/<int:pk>/update/', views.CityUpdateUV.as_view(), name='city_update', ),

    # /city/city/99/delete/
    path('city/<int:pk>/delete/', views.CityDeleteV.as_view(), name='city_delete', ),

    # /city/intersection/add/
    path('intersection/add/', views.IntersectionAddCV.as_view(), name='intersection_add', ),

    # /city/intersection/change/
    path('intersection/change/', views.IntersectionChangeLV.as_view(), name='intersection_change', ),

    # /city/intersection/99/update/
    path('intersection/<int:pk>/update/', views.IntersectionUpdateUV.as_view(), name='intersection_update', ),

    # /city/intersection/99/delete/
    path('intersection/<int:pk>/delete/', views.IntersectionDeleteV.as_view(), name='intersection_delete', ),

    # /city/intersection/stat/
    path('intersection/stat/', views.IntersectionLVStat.as_view(), name='intersection_stat', ),


    # 교차로 A/S 이력 정보
    # /city/intersection/aslog/add/99/99/
    path('intersection/aslog/add/<int:city_no>/<int:int_no>/', views.ASLogAddCV.as_view(), name='aslog_add', ),

    # /city/intersection/aslog/detail/99/99/
    path('intersection/aslog/detail/<int:city_no>/<int:int_no>/', views.ASLogDetailLV.as_view(), name='aslog_detail', ),

    # /city/intersection/aslog/list/
    path('intersection/aslog/list/', views.ASLogLV.as_view(), name='aslog_list', ),

    # /city/intersection/aslog/change/
    path('intersection/aslog/change/', views.ASLogChangeLV.as_view(), name='aslog_change', ),

    # /city/intersection/99/update/
    path('intersection/aslog/<int:pk>/update/', views.ASLogUpdateUV.as_view(), name='aslog_update', ),

    # /city/intersection/99/delete/
    path('intersection/aslog/<int:pk>/delete/', views.ASLogDeleteV.as_view(), name='aslog_delete', ),

    # 기타 기능들
    # 미세먼지 측정 결과 처리 (실시간, 시간대별, 일별)
    # /city/intersection/dustlog/list/
    path('intersection/dustlog/list/', views.DustLogLV.as_view(), name='dustlog_list', ),
    path('intersection/dustlog/hour/list/', views.DustLogHourLV.as_view(), name='dustlog_hour_list', ),
    path('intersection/dustlog/day/list/', views.DustLogDayLV.as_view(), name='dustlog_day_list', ),
]