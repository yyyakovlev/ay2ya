from django.shortcuts import render

# Create your views here.
def view(req):
    return render(req, "index.html")