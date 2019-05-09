from django.shortcuts import render
from .models import Usuario # Importa el modelo
from django.http import Http404 # Importa vista de error 404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, render_to_response

# Create your views here.

def index(request):
    return render(request, 'MundoFastWebApp/index.html')

def usuarios(request):
    listaUsuario = Usuario.objects.order_by('-rutUsuario')
    context = {'listaUsuario': listaUsuario}
    return render(request, 'MundoFastWebApp/Usuario/usuarios.html', context)

def verUsuario(request, id):
    try:
        usuario = Usuario.objects.get(pk=id)
    except Usuario.DoesNotExist:
        raise Http404("Error. Usuario no existe.")
    return render(request, 'MundoFastWebApp/Usuario/verUsuario.html', {'usuario': usuario})

def formUsuario(request):
    return render(request, 'MundoFastWebApp/Usuario/crearUsuario.html')

def crearUsuario(request):
    try:
        usuario = Usuario(rutUsuario = request.POST['rutUsuario'], nombreUsuario = request.POST['nombreUsuario'], emailUsuario = request.POST['emailUsuario'], imagenUsuario = request.POST['imagenUsuario'], rolUsuario = request.POST['rolUsuario'], passwordUsuario = request.POST['passwordUsuario'])
    except (KeyError, Usuario.DoesNotExist):
        return render(request, 'MundoFastWebApp/Usuario/crearUsuario.html', {'usuario': usuario, 'error_message': 'Error al crear Nuevo Usuario',})
    else:
        usuario.save()
        return HttpResponseRedirect(reverse('MundoFastWebApp:usuarios'))

def modificarUsuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    if request.method == 'POST':
        usuario.rutUsuario = request.POST['rutUsuario']
        usuario.nombreUsuario = request.POST['nombreUsuario']
        usuario.emailUsuario = request.POST['emailUsuario']
        usuario.imagenUsuario = request.POST['imagenUsuario']
        usuario.rolUsuario = request.POST['rolUsuario']
        usuario.passwordUsuario = request.POST['passwordUsuario']
        usuario.save()
        return HttpResponseRedirect(reverse('MundoFastWebApp:usuarios'))
    else:
        return render(request, 'MundoFastWebApp/Usuario/modificarUsuario.html', {'usuario': usuario})
