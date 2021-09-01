from django import forms
from .models import *


class AutorForm(forms.ModelForm): #Si usamos forms.Form tendremos que agregar los campos manualmente
    class Meta:
        model = Autor
        fields = ['nombre','apellidos','nacionalidad','descripcion']