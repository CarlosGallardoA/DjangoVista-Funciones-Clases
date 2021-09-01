from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from .models import *
# Create your views here.


def Home(request):
    return render(request, 'libro/home.html')


def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('home')
    else:
        autor_form = AutorForm()
    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form})


def listarAutor(request):
    autores = Autor.objects.filter(estado=True)
    return render(request, 'libro/listar_autores.html', {'autores': autores})


def editarAutor(request, id):
    autor_form = None
    error = None
    try:
        autor = Autor.objects.get(id=id)
        if request.method == 'GET':
            autor_form = AutorForm(instance=autor)
        else:
            autor_form = AutorForm(request.POST, instance=autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('home')
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form, 'error' : error})

def eliminarAutor(request, id):
    autor = Autor.objects.get(id = id)
    #--Eliminacion logica--
    #autor.estado = False
    #autor.save()
    autor.delete()
    return redirect('listar_autor')