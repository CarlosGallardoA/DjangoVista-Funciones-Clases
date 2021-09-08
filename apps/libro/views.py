from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from .models import *
from django.urls import reverse_lazy
##CLases 
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, View
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

#Usando funciones en vistas basadas en clases
class ListarLibros(View):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/listar_libros.html' #queryset default is Lobro.objects.all()

    def get_queryset(self):
        return self.model.objects.filter(estado = True)

    def get_context_data(self, **kwargs):
        context = {}
        context['libros'] = self.get_queryset
        context['form'] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name, self.get_context_data())

    
## Ahora libros

class CrearLibro(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/crear_libro.html'
    success_url = reverse_lazy('listar_libros')

class ActualizarLibro(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/libro.html'
    success_url = reverse_lazy('listar_libros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libros'] = Libro.objects.filter(estado = True)
        return context

class EliminarLibro(DeleteView):
    model = Libro
    def post(self, request, pk, *args, **kwargs):
        object = Libro.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('listar_libros')

