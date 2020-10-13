from django.views.generic import TemplateView

from django.views.generic import CreateView, ListView
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.contrib.auth.mixins import AccessMixin
from city2.models import Intersection

class HomeView(ListView):
    model = Intersection
    template_name = 'home.html'

# 2020-09-25 by fantasy8
# - UserRegistrationForm() 추가 : 사용자명, E-mail 정보 추가 처리 위해
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name')

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

