from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView as T

# def view_prj(req):
#     return render(req, "projects.html")

class ProjectsView(T):
    template_name = "projects.html"

# class ProjectsView(View):
#     def get(self, req):
#         return render(req, "projects.html")