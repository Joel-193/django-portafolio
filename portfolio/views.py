from django.shortcuts import render
from .models import Project
def home(request): #Primera vista de la pagina principal
    projects = Project.objects.all()
    return render(request, 'home.html',{'projects': projects})
