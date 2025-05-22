from django.contrib import admin
from django.urls import path
from myapp_empresa.views import recibe_ventas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('integracion/<str:sucursal>/<str:monto>/recibe_ventas/', recibe_ventas, name='recibe_ventas'),
]


