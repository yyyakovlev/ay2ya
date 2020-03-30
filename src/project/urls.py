rom pathlib import Path
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

here = Path(__file__).parent.resolve()

def view(r):
    index = here.parent.parent / "index.html"
    with index.open() as f:
        return HttpResponse(f.read())

def jpg(r):
    jpg = here.parent.parent / "pic/*.jpg"
    with jpg.open('rb') as f:
        return HttpResponse(f.read(), content_type="img/jpg")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jpg', view.jpg),
    path('', view),
]
