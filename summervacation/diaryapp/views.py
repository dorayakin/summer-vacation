from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Diary

# Create your views here.


class user_login(LoginView):
    template_name = 'diaryapp/login.html'
    redirect_authenticated_user = True


class user_logout(LogoutView):
    template_name = 'diaryapp/logout.html'


class home(LoginRequiredMixin, generic.ListView):
    template_name = 'diaryapp/home.html'
    context_object_name = 'latest_diary_list'

    def get_queryset(self):
        return Diary.objects.order_by('-pub_date')[:5]


class detail_view(LoginRequiredMixin, generic.DetailView):
    model = Diary
    template_name = 'diaryapp/detail.html'
