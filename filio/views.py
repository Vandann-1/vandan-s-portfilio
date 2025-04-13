from django.views.generic import TemplateView
from django.shortcuts import render
# from .models import About, Client, Contact  # Import only the necessary models
from .models import Resume



def home(request):
    clients= Resume.objects.first() 
    return render(request, 'home.html',{"clients":clients})










