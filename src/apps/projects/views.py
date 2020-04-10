from django.shortcuts import render

# Create your views here.
def view_prj(req):
    return render(req, "projects.html")