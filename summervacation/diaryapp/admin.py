from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import DiaryUser 
# Register your models here
class DiaryUserAdmin(admin.ModelAdmin):
    list_display = ('username', )
    search_fields = ('username', )

admin.site.register(DiaryUser,DiaryUserAdmin)