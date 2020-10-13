from django.forms import inlineformset_factory
from city2.models import City, Intersection

CityInlineFormSet = inlineformset_factory(City, Intersection,
    fields = ['model_name', 'man_company', 'make_date', 'cpu_version', 'cpu_bd_kind', 'case_status', 
            'bd_ins_kind', 'latitude', 'longitude', 'orientation', 'latitude2', 'longitude2', 'orientation2', 
            'image', 'image2', 'int_name', 'description', 'product_type'],
    extra = 2
)