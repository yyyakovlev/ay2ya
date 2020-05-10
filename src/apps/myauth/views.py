from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic import ListView

# from django.views.generic import TemplateView
#
# from apps.blog.models import BloggPost
#
# # def view_cv(req):
# #     return render(req, "cv.html")
#
# # class CvView(View):
# #     def get(self, req):
# #         return render(req, "cv.html")
#
# class BlogView(LoginRequiredMixin, ListView):
#     template_name = "blog.html"
#     # queryset = Project.objects.filter(is_hidden=False)
#     model = BloggPost
#
#
#
# class BlogPostView(LoginRequiredMixin, DetailView):
#     template_name = "post.html"
#     model = BloggPost
