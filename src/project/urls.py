from pathlib import Path
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

here = Path(__file__).parent.resolve()

def real_static (file, content_type):
    with file.open('rb') as f:
        return HttpResponse(f.read(), content_type)

def view(r):
    return real_static(here.parent.parent / "index.html", None)

    # index = here.parent.parent / "index.html"
    # with index.open() as f:
    #     return HttpResponse(f.read())

def jpg(r):
    return real_static(here.parent.parent / "src/pic/IMG-7655.jpg", "img/jpeg")

    # jpg = here.parent.parent / "src/pic/IMG-7655.jpg"
    # with jpg.open('rb') as f:
    #     return HttpResponse(f.read(), content_type="img/jpeg")

def jpg2(r):
    return real_static(here.parent.parent / "src/pic/computer-icons.jpg", "img/jpeg")

    # jpg2 = here.parent.parent / "src/pic/computer-icons.jpg"
    # with jpg2.open('rb') as f:
    #     return HttpResponse(f.read(), content_type="img/jpeg")

def jpg3(r):
    return real_static( here.parent.parent / "src/pic/ico-icon-ghost.jpg", "img/jpeg")

    # here.parent.parent / "src/pic/computer-icons.jpg"
    # jpg3 = here.parent.parent / "src/pic/ico-icon-ghost.jpg"
    # with jpg3.open('rb') as f:
    #     return HttpResponse(f.read(), content_type="img/jpeg")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jpg/', jpg),
    path('jpg2/', jpg2),
    path('jpg3/', jpg3),
    path('', view),
]

# def view1(r):
# открываем ФАЙЛ1
# читаем содержимое
# создаём HttpResponse
# с содержимым файла
# и ТИПОМ КОНТЕНТА1
# возвращаем из функции этот респонс