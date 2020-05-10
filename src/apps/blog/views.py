from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic import ListView

from apps.blog.models import BlogPost

# from django.views.generic import TemplateView


# def view_cv(req):
#     return render(req, "cv.html")

# class CvView(View):
#     def get(self, req):
#         return render(req, "cv.html")


class BlogView(LoginRequiredMixin, ListView):
    template_name = "blog.html"
    # queryset = Project.objects.filter(is_hidden=False)
    model = BlogPost


class BlogPostView(LoginRequiredMixin, DetailView):
    template_name = "post.html"
    model = BlogPost
