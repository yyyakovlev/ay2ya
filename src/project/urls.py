from pathlib import Path
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

here = Path(__file__).parent.resolve()

def view(r):
    index = here.parent.parent / "index.html"
    with index.open() as f:
        return HttpResponse(f.read())

def jpg(r):
    jpg = here.parent.parent / "src/pic/img-7655.jpg"
    with jpg.open('rb') as f:
        return HttpResponse(f.read(), content_type="img/jpeg")

def jpg2(r):
    jpg2 = here.parent.parent / "src/pic/computer-icons.jpg"
    with jpg2.open('rb') as f:
        return HttpResponse(f.read(), content_type="img/jpeg")

def jpg3(r):
    jpg3 = here.parent.parent / "src/pic/ico-icon-ghost.jpg"
    with jpg3.open('rb') as f:
        return HttpResponse(f.read(), content_type="img/jpeg")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jpg/', jpg),
    path('jpg2/', jpg2),
    path('jpg3/', jpg3),
    path('', view),
]
