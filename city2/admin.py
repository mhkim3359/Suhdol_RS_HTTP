from django.contrib import admin
from city2.models import City, Intersection

# Register your models here.

class IntersectionInline(admin.StackedInline):
    model = Intersection
    extra = 2

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    inlines = (IntersectionInline, )
    list_display = ('id', 'city_name', 'description', 'owner')

@admin.register(Intersection)
class IntersectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'int_name', 'model_name', 'make_date', 'cpu_version', 'owner')