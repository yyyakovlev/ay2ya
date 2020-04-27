from django import forms
from django.contrib import admin
# from django.contrib.admin import ModelAdmin
from apps.blog.models import BloggPost

from apps.cv.models import Techno
from apps.cv.models import Project
from apps.cv.models import Resposibility




# class UserInfoAdminForm(forms.ModelForm):
#     class Meta:
#         model = UserInfo
#         fields = "__all__"
#         widgets = {"name": forms.TextInput()}
#
# @admin.register(Techno)
# class CvAdminModel(ModelAdmin): #Появится в админке Джанго
#     pass
#
# @admin.register(Project)
# class CvAdminModel(ModelAdmin): #Появится в админке Джанго
#     pass

@admin.register(BloggPost)
class BloggPostAdminModel(admin.ModelAdmin): #Появится в админке Джанго
    pass