from django.shortcuts import get_object_or_404, render, render_to_response
from .models import Usuario # Importa el modelo
from django.http import Http404 # Importa vista de error 404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Producto

def index(request):
    return render(request, 'MundoFastWebApp/index.html')



def productos(request):
    listaProducto = Producto.objects.order_by('-id')
    context = {'listaProducto': listaProducto}
    return render(request, 'MundoFastWebApp/Producto/productos.html', context)

def verProducto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    return render(request, 'MundoFastWebApp/Producto/verProducto.html', {'producto': producto})

def formProducto(request):
    producto = Producto()
    return render(request, 'MundoFastWebApp/Producto/crearProducto.html', {'producto': producto})

def crearProducto(request):
    try:
        producto = Producto(codigoProducto = request.POST['codigoProducto'], nombreProducto = request.POST['nombreProducto'], 
            descripcionProducto = request.POST['descripcionProducto'], categoriaProducto = request.POST['categoriaProducto'], 
            precioProducto = request.POST['precioProducto'],cantidadProducto = request.POST['cantidadProducto'],
            ofertaProducto = request.POST['ofertaDropDown'],descuentoProducto = request.POST['descuentoProducto'])
    except IntegrityError:
        return render(request, "MundoFastWebApp/Producto/crearProducto.html", {"error_message": "Dejaste un campo vacío"})
    else:
        producto.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('MundoFastWebApp:productos'))

def modificarProducto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        producto.codigoProducto = request.POST['codigoProducto']
        producto.nombreProducto = request.POST['nombreProducto']
        producto.descripcionProducto = request.POST['descripcionProducto']
        producto.categoriaProducto = request.POST['categoriaProducto']
        producto.precioProducto = request.POST['precioProducto']
        producto.cantidadProducto = request.POST['cantidadProducto']
        producto.ofertaProducto = request.POST['ofertaDropDown']
        producto.descuentoProducto = request.POST['descuentoProducto']
        producto.save()
        return HttpResponseRedirect(reverse('MundoFastWebApp:productos'))
    else:
        return render(request, 'MundoFastWebApp/Producto/modificarProducto.html', {'producto': producto})

def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        if 'opcionSi' in request.POST:
            producto.delete()
        return HttpResponseRedirect(reverse('MundoFastWebApp:productos'))
    else:
        return render(request, 'MundoFastWebApp/Producto/eliminarProducto.html', {'producto': producto})

def ofertaProducto(request):
    listaProducto = [producto for producto in Producto.objects.order_by('-id') if producto.ofertaProducto]
    context = {'listaProducto': listaProducto}
    return render(request, 'MundoFastWebApp/Producto/ofertaProducto.html', context)

def buscarProducto(request):
    listaProducto = [producto for producto in Producto.objects.order_by('-id') if request.POST['buscarProducto'] in producto.nombreProducto]
    context = {'listaProducto': listaProducto}
    return render(request, 'MundoFastWebApp/Producto/productos.html', context)
    
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

