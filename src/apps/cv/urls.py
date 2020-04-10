from django.urls import path
from apps.cv.views import view_cv

urlpatterns = [
    path('view_cv/', view_cv),
]