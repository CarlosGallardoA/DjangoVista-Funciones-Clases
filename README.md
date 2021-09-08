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
## Si la relacion de modelos de ManyToMany para mostrar los datos en la vista tienes que usar la
```html
<td>
    {% for autor in libro.autor_id.all %}
        <li>{{ autor.nombre }}</li>
    {% endfor %}
</td>
```
## Para la eliminacion con clases se usa
```python
class EliminarLibro(DeleteView):
    model = Libro
    def post(self, request, pk, *args, **kwargs):
        object = Libro.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('listar_libros')
```
## Esto necesita crear un modelo_confirm_delete.html 
```html
<form method="POST">
    {% csrf_token %}
    <p><strong>¿Desea eliminar el registro {{ object }} ?</strong></p>
    <button type="submit" class="btn btn-danger">Confirmar</button>
</form>
```
## Escalar codigo usando funciones dentro de las vistas basadas en clases
```python
class ListarLibros(View):
    model = Libro
    template_name = 'libro/libro/listar_libros.html'
    #get_queryset es para la consulta
    def get_queryset(self):
        return self.model.objects.filter(estado = True)
    #el get_context_data es para definir el contexto a pasar a la vista
    def get_context_data(self, **kwargs):
        context = {}
        context['libros'] = self.get_queryset
        return context
    #Usamos el metodo get para recibir la info
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name, self.get_context_data())
```
### Recordar si solo pasamos:
```python
form = self.form_class(request.POST)
```
### es para agregar un nuevo registro pero si pasamos:
```python
form = self.form_class(request.POST, intance = consulta)
```
### es para editar
## importante el object es un objecto que se crea automaticamente al momento de usar :
```python
context = super().get_context_data(**kwargs)
```
## Jquery usar modal:
```js
function abrir_modal_edicion(url){
        $('#edicion').load(url, function(){
            $(this).modal('show');
        })
    }

```