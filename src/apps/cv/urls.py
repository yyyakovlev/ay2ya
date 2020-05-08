from django.urls import path

# from apps.cv.apps import CvConfig
from apps.cv.views import CvView

# app_name = CvConfig.label

urlpatterns = [
    path("", CvView.as_view(), name="cv"),
]
