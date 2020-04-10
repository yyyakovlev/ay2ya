
from django.urls import path
from apps.index.views import view

urlpatterns = [
    path('', view),

]