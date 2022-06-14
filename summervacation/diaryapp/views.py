from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.


class user_login(LoginView):
    template_name = 'diaryapp/login.html'
    redirect_authenticated_user = True


class home(LoginRequiredMixin,TemplateView):
    template_name = 'diaryapp/home.html'


class user_logout(LogoutView):
    template_name = 'diaryapp/logout.html'
