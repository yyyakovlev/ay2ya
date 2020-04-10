from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# def view(req):
#     return render(req, "index.html")

class IndexView(TemplateView):
    template_name = "index.html"

    # def get(self, req):
    #     return render(req, "index.html")