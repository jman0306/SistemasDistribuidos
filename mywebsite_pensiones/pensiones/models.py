from django.db import models

class TrabajadorIndependiente(models.Model):
    nombre = models.CharField(max_length=100)
    edad_actual = models.IntegerField()
    edad_retiro = models.IntegerField()
    saldo_afore = models.FloatField()
    ahorro_mensual = models.FloatField()
    genero = models.CharField(max_length=10)

    def calcular_pension_mensual(self):
        años_restantes = self.edad_retiro - self.edad_actual
        if años_restantes <= 0:
            return 0  # Ya se retiró o edad inválida

        total_ahorrado = self.saldo_afore + (self.ahorro_mensual * 12 * años_restantes)
        # Supongamos que la pensión mensual es el total dividido entre 20 años de retiro (240 meses)
        pension_mensual = total_ahorrado / 240
        return round(pension_mensual, 2)

