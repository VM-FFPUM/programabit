from django import forms
from django.forms import ModelForm
from publicar.models import Anuncio, Propuesta
from registrar.models import Cliente, Trabajador
from django.contrib.auth.forms import UserCreationForm
import datetime


class AnuncioForm(ModelForm):

    titulo = forms.CharField(min_length=5, max_length=50)
    precio_estimado = forms.CharField(max_length=8)

    class Meta:
        model = Anuncio
        fields = ['titulo', "cliente", 'fecha_limite', 'precio_estimado', 'zona', 'descripcion', 'habilidades_requeridas']

class PropuestaForm(ModelForm):

    class Meta:
        model = Propuesta
        fields = ['oferta', 'tiempo_estimado']


class ClienteForm(UserCreationForm):

    class Meta:
        model = Cliente
        fields = ['username', 'email', 'password1', 'password2', 'zona']

class TrabajadorForm(UserCreationForm):

    class Meta:
        model = Trabajador
        fields = ['username', 'email', 'password1', 'password2', 'zona', 'descripcion', 'habilidades']
