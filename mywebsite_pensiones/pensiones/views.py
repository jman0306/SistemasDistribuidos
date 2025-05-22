from django.shortcuts import render
from .forms import TrabajadorForm
from .models import Trabajador

def inicio(request):
    if request.method == 'POST':
        if 'limpiar' in request.POST:
            form = TrabajadorForm()
        elif 'agregar' in request.POST:
            form = TrabajadorForm(request.POST)
            if form.is_valid():
                trabajador = form.save()
                pension = trabajador.calcular_pension_mensual()
                return render(request, 'resultado.html', {
                    'trabajador': trabajador,
                    'pension': pension
                })
    else:
        form = TrabajadorForm()
    return render(request, 'index.html', {'form': form})  # Usamos index.html

def listado(request):
    criterio = request.GET.get('orden', 'nombre')
    trabajadores = Trabajador.objects.all().order_by(criterio)
    return render(request, 'listado.html', {
        'trabajadores': trabajadores
    })

