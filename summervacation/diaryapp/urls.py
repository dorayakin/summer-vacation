from django.urls import path
from . import views
app_name = 'diaryapp'
urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('login/', views.user_login.as_view(), name='login'),
    path('logout/', views.user_logout.as_view(), name='logout'),
    path('home/', views.home.as_view(), name='home'),
    path('<int:pk>/detail/', views.detail_view.as_view(), name='detail'),
    path('create/', views.create_diary.as_view(), name='create'),
    path('<int:pk>/edit/', views.edit_diary.as_view(),name ='edit'),
]
