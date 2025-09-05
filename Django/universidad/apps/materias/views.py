from django.shortcuts import render
from .models import Materia

def lista_materias(request):
    materias = Materia.objects.all()
    return render(request, "materias/lista_materias.html", {"materias": materias})