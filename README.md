# Vistas basadas en funciones
## Usando la bibliteca forms de python 
## Usando from django.contrib.auth.views import LoginView para el login
```python
path('accounts/login/',LoginView.as_view(template_name ='login.html'), name='login'),
```
## Usando from django.contrib.auth.views import LogoutView para el login
```python
path('logout/',LogoutView.as_view(), name='logout')
```
## Usando decorador para proteger rutas from django.contrib.auth.decorators import login_required
```python
path('listar_autor',login_required(views.ListarAutor.as_view()), name='listar_autor'),
```
