from django.urls import path

from apps.zparser.views import ZparserView

urlpatterns = [
    path("", ZparserView.as_view(), name="zparser"),
]
