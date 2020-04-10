from django.urls import path
from apps.projects.views import view_prj

urlpatterns = [
    path('view_prj/', view_prj),
]