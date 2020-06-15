from pathlib import Path

from django.contrib import admin
from django.http import HttpResponse
from django.urls import include
from django.urls import path

#
# from src.apps.index.views import view
# from apps.cv.views import view_cv
# from apps.projects.views import view_prj

PROJECT_DIR = Path(__file__).parent.resolve()
BASE_DIR = PROJECT_DIR.parent.resolve()
REPO_DIR = BASE_DIR.parent.resolve()
STATIC_ROOT = REPO_DIR / ".static"


def r_static(fn, content_type):
    with fn.open("rb") as f:
        return HttpResponse(f.read(), content_type)


# def dj(r):
#     return r_static( here.parent.parent / "src/pic/dj.png", "img/jpeg")


def dj(r):
    return r_static(STATIC_ROOT / "dj.png", "img/jpeg")


def jpg(r):
    return r_static(STATIC_ROOT / "django.png", "img/jpeg")


def gmail(r):
    return r_static(STATIC_ROOT / "gmail.png", "img/jpeg")


def telega(r):
    return r_static(STATIC_ROOT / "telegram.png", "img/jpeg")


def body_bg(r):
    return r_static(STATIC_ROOT / "body.jpg", "img/jpeg")


def header_bg(r):
    return r_static(STATIC_ROOT / "header.jpg", "img/jpeg")


def comp_lx(r):
    return r_static(STATIC_ROOT / "comp_lx.png", "img/jpeg")


def comp_tl(r):
    return r_static(STATIC_ROOT / "comp_tl.png", "img/jpeg")


def comp_rfi(r):
    return r_static(STATIC_ROOT / "comp_rfi.png", "img/jpeg")


def comp_tms(r):
    return r_static(STATIC_ROOT / "comp_tms.jpg", "img/jpeg")


def cv_pdf(r):
    return r_static(STATIC_ROOT / "my_cv.pdf", "pdf")


def video_bot(r):
    return r_static(STATIC_ROOT / "bot_replay.mp4", "video/mp4")


def video_x0(r):
    return r_static(STATIC_ROOT / "x0_game.mp4", "video/mp4")


urlpatterns = [
    path("grappelli/", include("grappelli.urls")),  # grappelli URLS
    path("admin/", admin.site.urls),
    # path('sentry-debug/', trigger_error),
    path("jpg/", jpg),
    path("dj/", dj),
    path("gmail/", gmail),
    path("telega/", telega),
    path("body_bg/", body_bg),
    path("comp_lx/", comp_lx),
    path("comp_tl/", comp_tl),
    path("comp_rfi/", comp_rfi),
    path("comp_tms/", comp_tms),
    path("cv_pdf/", cv_pdf),
    path("video_bot/", video_bot),
    path("video_x0/", video_x0),
    path("header_bg/", header_bg),
    path("", include("apps.index.urls")),
    path("", include("apps.api.urls")),
    path("account/", include("allauth.urls")),
    path("indx/", include("apps.index.urls")),
    path("login/", include("apps.myauth.urls")),
    path("logout/", include("apps.myauth.urls")),
    path("view_blg/", include("apps.blog.urls")),
    path("view_cv/", include("apps.cv.urls")),
    path("view_prj/", include("apps.projects.urls")),
    path("view_zparser/", include("apps.zparser.urls")),
    path("subscription/", include("apps.subscription.urls")),
]
