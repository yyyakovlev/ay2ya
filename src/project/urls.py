from pathlib import Path
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render

here = Path(__file__).parent.resolve()

def r_static (fn, content_type):
    with fn.open('rb') as f:
        return HttpResponse(f.read(), content_type)

# def view(r):
#     return r_static(here.parent.parent / "PROJECT_DIR/templates/index.html", None)

def view(req):
    return render(req, "index.html")

def view_cv(req):
    return render(req, "cv.html")

def view_prj(req):
    return render(req, "projects.html")
#
# def view_ct(req):
#     return render(req, "contacts.html")

    # index = here.parent.parent / "index.html"
    # with index.open() as f:
    #     return HttpResponse(f.read())

def dj(r):
    return r_static( here.parent.parent / "src/pic/dj.png", "img/jpeg")

def jpg(r):
    return r_static(here.parent.parent / "src/pic/IMG-7655.jpg", "img/jpeg")

    # jpg = here.parent.parent / "src/pic/IMG-7655.jpg"
    # with jpg.open('rb') as f:
    #     return HttpResponse(f.read(), content_type="img/jpeg")

def gmail(r):
    return r_static(here.parent.parent / "src/pic/gmail.png", "img/jpeg")


def telega(r):
    return r_static( here.parent.parent / "src/pic/telegram.png", "img/jpeg")

def body_bg(r):
    return r_static( here.parent.parent / "src/pic/body.jpg", "img/jpeg")

def header_bg(r):
    return r_static( here.parent.parent / "src/pic/header.jpg", "img/jpeg")




urlpatterns = [
    path('admin/', admin.site.urls),
    path('jpg/', jpg),
    path('dj/', dj),
    path('gmail/', gmail),
    path('telega/', telega),
    path('body_bg/', body_bg),
    path('header_bg/', header_bg),
    path('', view),
    path('indx/', view),
    path('view_cv/', view_cv),
    path('view_prj/', view_prj),
    # path('view_ct/', view_ct),
]

# def view1(r):
# открываем ФАЙЛ1
# читаем содержимое
# создаём HttpResponse
# с содержимым файла
# и ТИПОМ КОНТЕНТА1
# возвращаем из функции этот респонс