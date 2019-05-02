from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario # Importa el modelo
from django.template import loader # Importa el template
from django.http import Http404 # Importa vista de error 404

# Create your views here.

def index(request):
    return render(request, 'MundoFastWebApp/index.html')

def usuarios(request):
    listaUsuario = Usuario.objects.order_by('-rutUsuario')
    template = loader.get_template('MundoFastWebApp/usuarios.html')
    context = {
        'listaUsuario': listaUsuario,
    }
    return render(request, 'MundoFastWebApp/usuarios.html', context)

def verUsuario(request, id):
    try:
        usuario = Usuario.objects.get(pk=id)
    except Usuario.DoesNotExist:
        raise Http404("Error. Usuario no existe.")
    return render(request, 'MundoFastWebApp/verUsuario.html', {'usuario': usuario})

def crearUsuario(request):
    return render(request, 'MundoFastWebApp/crearUsuario.html')

