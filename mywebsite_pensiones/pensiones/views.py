# views.py
from django.shortcuts import render, redirect
from .models import TrabajadorIndependiente

def index(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        edad_actual = int(request.POST.get('edad_actual'))
        edad_retiro = int(request.POST.get('edad_retiro'))
        saldo_afore = float(request.POST.get('saldo_afore'))
        ahorro_mensual = float(request.POST.get('ahorro_mensual'))
        genero = request.POST.get('genero')

        trabajador = TrabajadorIndependiente.objects.create(
            nombre=nombre,
            edad_actual=edad_actual,
            edad_retiro=edad_retiro,
            saldo_afore=saldo_afore,
            ahorro_mensual=ahorro_mensual,
            genero=genero
        )
        pension = trabajador.calcular_pension_mensual()

        return render(request, 'resultado.html', {
            'trabajador': trabajador,
            'pension': pension
        })

    return render(request, 'index.html')
