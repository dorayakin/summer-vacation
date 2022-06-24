from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
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
        return Diary.objects.order_by('-pub_date')[:10]


class detail_view(LoginRequiredMixin, generic.DetailView):
    model = Diary
    template_name = 'diaryapp/detail.html'


class create_diary(LoginRequiredMixin, generic.CreateView):
    model = Diary
    template_name = 'diaryapp/create.html'
    fields = ['title', 'main_text', 'public_mode']

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('diaryapp:detail', kwargs={'pk': self.object.pk})


class edit_diary(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Diary
    template_name = 'diaryapp/edit.html'
    fields = ['title', 'main_text', 'public_mode']

    def test_func(self):
        diary = self.get_object()
        if self.request.user == diary.writer:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('diaryapp:detail', kwargs={'pk': self.object.pk})
