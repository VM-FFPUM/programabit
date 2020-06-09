from django.contrib import admin
from .models import Anuncio, Propuesta

class AnuncioAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'precio_estimado']

class PropuestaAdmin(admin.ModelAdmin):
    list_display = ['oferta', 'tiempo_estimado']

admin.site.register(Anuncio)
admin.site.register(Propuesta)
