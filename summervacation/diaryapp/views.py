import logging
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic

from .forms import DiaryForm
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


class create_diary(LoginRequiredMixin, generic.CreateView):
    model = Diary
    template_name = 'diaryapp/create.html'
    form_class = DiaryForm
    success_url = 'diaryapp:home'


class edit_diary(UserPassesTestMixin, generic.UpdateView):
    model = Diary
    template_name = 'diaryapp/edit.html'
    form_class = DiaryForm
    succsess_url = 'diary:home'
    
    def test_func(self):
        diary_writer = self.model.objects.get(writer=self.kwargs['pk'])
        logging.info(diary_writer.writer.id)
        if self.request.user.id == diary_writer.writer.id:
            return True 
