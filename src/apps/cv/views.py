from django.shortcuts import render

# Create your views here.
def view_cv(req):
    return render(req, "cv.html")