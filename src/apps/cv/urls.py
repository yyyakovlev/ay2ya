from django.urls import path
from apps.cv.views import CvView

urlpatterns = [
    path('', CvView.as_view()),
]