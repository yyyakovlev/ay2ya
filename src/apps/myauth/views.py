# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import DetailView
# # from django.views.generic import ListView
# #
# # from django.views.generic import TemplateView
# #
# from apps.myauth.models import MyAuth
#
# # # def view_cv(req):
# # #     return render(req, "cv.html")
# #
# # # class CvView(View):
# # #     def get(self, req):
# # #         return render(req, "cv.html")
# #
# class MyAuthLoginView(LoginRequiredMixin, ListView):
#     template_name = "login.html"
#     # queryset = Project.objects.filter(is_hidden=False)
#     model = MyAuth
#
#
# class MyAuthLogoutView(LoginRequiredMixin, ListView):
#     template_name = "logged_out.html"
#     # queryset = Project.objects.filter(is_hidden=False)
#     model = MyAuth
# #
#
#
# class BlogPostView(LoginRequiredMixin, DetailView):
#     template_name = "post.html"
#     model = BloggPost
