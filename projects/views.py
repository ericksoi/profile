from django.shortcuts import render
from .models import Project 
from django.utils import timezone
# Create your views here.


def project_list(request):
    project = Project.objects.all()
    return render(request, 'projects/project_list.html', {'project': project})
