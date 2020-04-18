from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# def view(req):
#     return render(req, "index.html")
from apps.index.models import UserInfo


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):

        # parent_ctx=TemplateView.get_context_data()
        parent_ctx = super().get_context_data() #super - обращение к родителю

        info = UserInfo.objects.first()

        ctx = {"name": info.name, "grts": info.grts, "age": info.age}

        ctx.update(parent_ctx)

        return ctx



    # def get(self, req):
    #     return render(req, "index.html")