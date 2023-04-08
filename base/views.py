from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Project
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
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
    if request.method == 'POST':
        send_email(request)

    return render(request, 'index.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def send_email(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        contact = Contact(full_name=full_name, email=email, mobile_number=mobile_number, subject=subject, message=message)
        contact.save()
        
        messages.success(request, 'Your message has been sent!')
        return redirect('/#contact')
    
    return render(request, 'main.html')
