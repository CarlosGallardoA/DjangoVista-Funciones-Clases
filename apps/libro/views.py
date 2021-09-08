from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from .models import *
from django.urls import reverse_lazy
##CLases 
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
# Create your views here.
'''
dispatch(): Valida la peticion y elige que metodo HTTP se utilizo para la solicitud
http_method_not_allowed(): retorna un error cuando se utiliza un metodo HTTP no soportado o definido
'''
class Inicio(TemplateView):
    template_name = 'libro/home.html'
'''
class ListarAutor(TemplateView):
    template_name = 'libro/listar_autores.html'
    def get(self, request, *args, **kwargs):
        autores = Autor.objects.filter(estado = True)
        return render(request, self.template_name, {'autores': autores})
'''
class ListarAutor(ListView):
    model = Autor
    template_name = 'libro/autor/listar_autores.html'
    #Nombre para el contexto a enviar, si no lo definimos se pasa como object_list
    context_object_name = 'autores'
    queryset = Autor.objects.filter(estado = True)

class ActualizarAutor(UpdateView):
    model = Autor
    template_name = 'libro/autor/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('listar_autor')

class CrearAutor(CreateView):
    model = Autor
    template_name = 'libro/autor/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('listar_autor')

class EliminarAutor(DeleteView):
    model = Autor
    #Para eliminar de la base de datos
    #success_url = reverse_lazy('listar_autor')
    #Para eliminacion logica (estado de true a false)
    def post(self,request,pk, *args, **kwargs):
        object = Autor.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('listar_autor')


class ListarLibros(ListView):
    model = Libro
    template_name = 'libro/libro/listar_libros.html' #queryset default is Lobro.objects.all()
    queryset = Libro.objects.filter(estado = True)
    context_object_name = 'libros'
    
## Ahora libros

class CrearLibro(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/crear_libro.html'
    success_url = reverse_lazy('listar_libros')

class ActualizarLibro(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/crear_libro.html'
    success_url = reverse_lazy('listar_libros')

class EliminarLibro(DeleteView):
    model = Libro
    def post(self, request, pk, *args, **kwargs):
        object = Libro.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('listar_libros')

