from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

title="HDInformatica Soluciones"
description="Soluciones informáticas a distancia, consultorías, \
cursos online y edición de videos, redacción de proyectos y manejo de redes sociales."

class MainWebSite(object):
    
    def __init__(self, title, description):
        self.title=title
        self.description=description

def welcome(request):
    courses_available=["Excel", "Word", "PowerPoint"]
    ws=MainWebSite(title, description)

    file=loader.get_template('index.html')
    template=file.render()

    return render(
        request, 
        'index.html', 
        {"main_title" : ws.title, "main_description" : ws.description, "curses" : courses_available}
        )

def services(request):
    return render(
        request,
        'services.html'
    )