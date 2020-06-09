from django.contrib import admin
from .models import Trabajador, Cliente

class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'zona', 'calificacion_trabajador']

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'zona', 'calificacion_cliente']

admin.site.register(Cliente)
admin.site.register(Trabajador)
