from django.shortcuts import render
from .models import Skill, Project, Achievement

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    achievements = Achievement.objects.all()
    return render(request, 'portfolio/home.html', {
        'skills': skills,
        'projects': projects,
        'achievements': achievements
    })

def contact(request):
    if request.method == 'POST':
       
        pass
    return render(request, 'portfolio/contact.html')
