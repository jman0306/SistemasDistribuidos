from django.contrib import admin
from django.urls import path
from pensiones import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('listado/', views.listado, name='listado'),
]
