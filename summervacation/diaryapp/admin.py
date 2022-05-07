from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import DiaryUser, Diary
# Register your models here


class DiaryUserAdmin(UserAdmin):
    list_display = ("class_id", "username",
                    "last_name", "first_name", "is_active", "last_login")
    list_display_links = ("username",)
    ordering = ("class_id", )
    search_fields = ("username", "class_id")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {
         "fields": ("class_id", "first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


class DiaryAdmin(admin.ModelAdmin):
    list_display = ("title", "pub_date", "writer", "public_mode")
    list_filter = ["pub_date", "public_mode"]
    search_fields = ["title", "main_text", "writer__username"]
    search_help_text = "title,main_text,writerで検索できます"


admin.site.register(DiaryUser, DiaryUserAdmin)
admin.site.register(Diary, DiaryAdmin)
