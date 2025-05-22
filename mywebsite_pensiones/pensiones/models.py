from django.db import models

class Trabajador(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    nombre = models.CharField(max_length=100)
    genero = models.CharField(
        max_length=1,
        choices=GENERO_CHOICES,
        default='M'  # Valor por defecto para nuevas filas o migraciones
    )
    edad_actual = models.PositiveIntegerField()
    edad_retiro = models.PositiveIntegerField()
    saldo_acumulado = models.FloatField()
    ahorro_mensual = models.FloatField()

    def calcular_pension_mensual(self):
        meses = (self.edad_retiro - self.edad_actual) * 12
        if meses <= 0:
            return 0
        saldo_futuro = self.saldo_acumulado + (self.ahorro_mensual * meses)
        return round(saldo_futuro / 240, 2)  # 20 años de retiro
