from django.urls import path
from . import views 
urlpatterns = [
    path('', views.Inicio.as_view(), name='home'),
    path('crear_autor',views.CrearAutor.as_view(), name='crear_autor'),
    path('listar_autor',views.ListarAutor.as_view(), name='listar_autor'),
    path('editar_autor/<int:pk>',views.ActualizarAutor.as_view(), name='editar_autor'),
    path('eliminar_autor/<int:pk>',views.EliminarAutor.as_view(), name='eliminar_autor'),
]
