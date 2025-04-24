from django.shortcuts import render
from django.http import HttpResponse
from .models import Estudiante
from django.shortcuts import get_object_or_404



# Create your views here.
def index(request):
    return HttpResponse("Hola a todos desde myfirstapp")
def detalles(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
    carreras = estudiante.carrera_set.all()
    return render(request, "myfirstapp/detalles.html", 
    {"estudiante": estudiante,"carreras": carreras} )
def carreras(request, estudiante_id):
    return HttpResponse("Carreras del estudiante %s." % estudiante_id)
def index(request):
    estudiantes = Estudiante.objects.order_by("nombre")
    context = {
    "estudiantes": estudiantes,
    }
    return render(request, "myfirstapp/index.html", 
    context)
def agrega_carrera(request, estudiante_id, tipo, nombre):
    estudiante = Estudiante.objects.get(pk=estudiante_id)
    estudiante.carrera_set.create(tipo = int(tipo), nombre=nombre)
    return HttpResponse("Carrera agregada al estudiante %s" % estudiante_id)
def agrega_estudiante(request, nombre, apellidos, edad, foraneo, promedio):
    foraneo = foraneo.lower() == "true"
    estudiante = Estudiante( nombre=nombre, 
    apellidos=apellidos, 
    edad=int(edad), 
    foraneo=foraneo, 
    promedio=float(promedio))
    estudiante.save()
    return HttpResponse("Estudiante %s agregado exitósamente" % 
    estudiante.id)
def borra_estudiante(request, estudiante_id):
    estudiante = Estudiante.objects.get(pk=estudiante_id)
    estudiante.delete()
    return HttpResponse("Estudiante %s borrado exitósamente" % estudiante_id)
def edita_estudiante(request, estudiante_id, promedio):
    estudiante = Estudiante.objects.get(pk=estudiante_id)
    estudiante.promedio = float(promedio)
    estudiante.save() 
    return HttpResponse("El promedio del estudiante %s se ha actualizado exitósamente" % estudiante.id)
def agrega_estudiante_forma(request):
    nombre = request.POST.get("nombre")
    apellidos = request.POST.get("apellidos")
    edad = int(request.POST.get("edad"))
    if "foraneo" in request.POST:
        foraneo = True
    else:
        foraneo = False
        promedio = float(request.POST.get("promedio"))
        estudiante = Estudiante( nombre=nombre, 
        apellidos=apellidos, 
        edad=int(edad), 
        foraneo=foraneo, 
        promedio=float(promedio))
        estudiante.save()
    return HttpResponse("Estudiante %s agregado exitósamente desde la forma" % estudiante.id)

