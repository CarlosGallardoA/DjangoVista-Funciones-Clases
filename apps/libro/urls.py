from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views 
urlpatterns = [
    path('', login_required(views.Inicio.as_view()), name='home'),
    path('crear_autor/',login_required(views.CrearAutor.as_view()), name='crear_autor'),
    path('listar_autor/',login_required(views.ListarAutor.as_view()), name='listar_autor'),
    path('editar_autor/<int:pk>/',login_required(views.ActualizarAutor.as_view()), name='editar_autor'),
    path('eliminar_autor/<int:pk>/',login_required(views.EliminarAutor.as_view()), name='eliminar_autor'),

    path('listar_libros/', login_required(views.ListarLibros.as_view()), name='listar_libros'),
    path('crear_libro/', login_required(views.CrearLibro.as_view()), name='crear_libro'),
    path('editar_libro/<int:pk>/', login_required(views.ActualizarLibro.as_view()), name='editar_libro'),
    path('eliminar_libro/<int:pk>/', login_required(views.EliminarLibro.as_view()), name='eliminar_libro'),
]
