from pathlib import Path


from django.contrib import admin
from django.http import HttpResponse
from django.urls import include
from django.urls import path
#
# from src.apps.index.views import view
# from apps.cv.views import view_cv
# from apps.projects.views import view_prj

here = Path(__file__).parent.resolve()

def r_static (fn, content_type):
    with fn.open('rb') as f:
        return HttpResponse(f.read(), content_type)

def dj(r):
    return r_static( here.parent.parent / "src/pic/dj.png", "img/jpeg")

def jpg(r):
    return r_static(here.parent.parent / "src/pic/IMG-7655.jpg", "img/jpeg")

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
    path('', include('apps.index.urls')),
    path('indx/', include('apps.index.urls')),
    path('view_cv/', include('apps.cv.urls')),
    path('view_prj/', include('apps.projects.urls')),
]

# def view1(r):
# открываем ФАЙЛ1
# читаем содержимое
# создаём HttpResponse
# с содержимым файла
# и ТИПОМ КОНТЕНТА1
# возвращаем из функции этот респонс