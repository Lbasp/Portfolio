from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('Home page')



def about(request):
    return HttpResponse('About')
def projects(request):
    return HttpResponse('Projects')

def contact(request):
    return HttpResponse('Contact')