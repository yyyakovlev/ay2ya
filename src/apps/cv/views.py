from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# def view_cv(req):
#     return render(req, "cv.html")

# class CvView(View):
#     def get(self, req):
#         return render(req, "cv.html")

class CvView(TemplateView):
    template_name = "cv.html"