from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

# from django.views.generic import TemplateView
from apps.cv.models import Project

# def view_cv(req):
#     return render(req, "cv.html")

# class CvView(View):
#     def get(self, req):
#         return render(req, "cv.html")


class CvView(ListView):
    template_name = "cv.html"
    # queryset = Project.objects.filter(is_hidden=False)
    model = Project

    def get_queryset(self):
        return self.model.objects.order_by("start")

    # def get_context_data(self, **kwargs):
    #
    #     ctx = super().get_context_data(**kwargs)  # super - обращение к родителю
    #
    #     projects = Project.objects.all()
    #
    #     ctx['project'] = projects
    #
    #     return ctx
