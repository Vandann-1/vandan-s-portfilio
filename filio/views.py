from django.views.generic import TemplateView
from django.shortcuts import render
# from .models import About, Client, Contact  # Import only the necessary models
from .models import Resume


from filio.models import Resume

def home(request):
    resume = Resume.objects.first()   # or .last() if you prefer
    return render(request, 'home.html', {"resume": resume})











