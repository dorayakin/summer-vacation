from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic

# Create your views here.


class user_login(LoginView):
    template_name = 'diaryapp/login.html'


class home(generic.TemplateView):
    template_name = 'diaryapp/home.html'


class user_logout(LogoutView):
    template_name = 'diaryapp/logout.html'
