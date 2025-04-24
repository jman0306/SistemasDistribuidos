from django.shortcuts import render
from django.http import HttpResponse
from .models import Estudiante
from django.shortcuts import get_object_or_404



# Create your views here.
def index(request):
    return HttpResponse("Hola a todos desde myfirstapp")
def detalles(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
    return render(request, "myfirstapp/detalles.html", 
    {"estudiante": estudiante})
def carreras(request, estudiante_id):
    return HttpResponse("Carreras del estudiante %s." % estudiante_id)
def agrega_carrera(request, estudiante_id):
    return HttpResponse("Agregando una carrera a %s." % estudiante_id)
def index(request):
    estudiantes = Estudiante.objects.order_by("nombre")
    context = {
    "estudiantes": estudiantes,
    }
    return render(request, "myfirstapp/index.html", 
    context)

