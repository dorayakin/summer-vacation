from django.urls import path
from .views import home, user_login
app_name = 'diaryapp'
urlpatterns = [
    path('', home.as_view(), name='home'),
    path('login/', user_login.as_view(), name='login'),
    path('home/', home.as_view(), name='home')
]
