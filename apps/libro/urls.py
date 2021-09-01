from django.urls import path
from . import views 
urlpatterns = [
    path('', views.Home, name='home'),
    path('crear_autor',views.crearAutor, name='crear_autor'),
    path('listar_autor',views.listarAutor, name='listar_autor'),
    path('editar_autor/<int:id>',views.editarAutor, name='editar_autor'),
    path('eliminar_autor/<int:id>',views.eliminarAutor, name='eliminar_autor'),
]
