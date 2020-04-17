from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.index.models import UserInfo

# Register your models here.


@admin.register(UserInfo)
class UserInfoAdmMod(ModelAdmin):
    pass

