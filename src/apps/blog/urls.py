from django.urls import path

from apps.blog import views
from apps.blog.apps import BlogConfig

app_name = BlogConfig.label

urlpatterns = [
    path("", views.BlogView.as_view(), name="all_post"),
    path("post/<int:pk>/", views.BlogPostView.as_view(), name="post"),
]
