# Vistas basadas en funciones
## Usando la bibliteca forms de python 
## Usando from django.contrib.auth.views import LoginView para el login
```python
path('accounts/login/',LoginView.as_view(template_name ='login.html'), name='login'),
```
## Usando from django.contrib.auth.views import LogoutView para el logout
```python
path('logout/',LogoutView.as_view(), name='logout')
```
## Usando decorador para proteger rutas from django.contrib.auth.decorators import login_required
```python
path('listar_autor',login_required(views.ListarAutor.as_view()), name='listar_autor'),
```
# Ahora hacer un login manual creado una app usuario
```python
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login
from django.http import HttpResponseRedirect

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('home')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    #Para validar cambios 
    def form_valid(self, form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)
```
## En urls
```python
path('accounts/login/',Login.as_view(), name='login'),
```
# Ahora hacer un logout manual en el app usuario
```python
def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
```
## En urls importar from django.contrib.auth.decorators import login_required
```python
path('logout/',login_required(logoutUsuario), name='logout'),
```
