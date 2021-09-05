from django import forms
from .models import *


class AutorForm(forms.ModelForm): #Si usamos forms.Form tendremos que agregar los campos manualmente
    class Meta:
        model = Autor
        fields = ['nombre','apellidos','nacionalidad','descripcion']
        #Personalizar etiquetas en el html
        labels = {
            'nombre' : 'Nombre del autor',
            'apellidos' : 'Apellidos del autor',
            'nacionalidad' : 'Nacionalidad del autor',
            'descripcion' : 'Descripcion',
        }
        #Agregarle estilos a los inputs en el html
        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos' : forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidad' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
        }