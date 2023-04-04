from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Project

# project = [
#     {'id':1, 'name': 'probemos1'},
#     {'id':2, 'name': 'miremos'},
# ]


def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

def projects(request):
    proyectos= Project.objects.all()
    return render(request, 'base/projects.html')

def contact(request):
    return render(request, 'base/contact.html')