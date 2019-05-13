from django.shortcuts import get_object_or_404, render, render_to_response
from .models import Usuario, Producto # Importa el modelo
from django.http import Http404 # Importa vista de error 404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib import messages # Librería para mensajes

# Create your views here.

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
        messages.success(request, 'Producto creado correctamente.')
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
        messages.success(request, 'Producto modificado correctamente.')
        return HttpResponseRedirect(reverse('MundoFastWebApp:productos'))
    else:
        return render(request, 'MundoFastWebApp/Producto/modificarProducto.html', {'producto': producto})

def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        if 'opcionSi' in request.POST:
            producto.delete()
            messages.error(request, 'Producto eliminado correctamente.')
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
        messages.success(request, 'Usuario creado correctamente.')
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
        messages.success(request, 'Usuario modificado correctamente.')
        return HttpResponseRedirect(reverse('MundoFastWebApp:usuarios'))
    else:
        return render(request, 'MundoFastWebApp/Usuario/modificarUsuario.html', {'usuario': usuario})

def eliminarUsuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    if request.method == 'POST':
        if 'opcionSi' in request.POST:
            usuario.delete()
            messages.error(request, 'Usuario eliminado correctamente.')
        return HttpResponseRedirect(reverse('MundoFastWebApp:usuarios'))
    else:
        return render(request, 'MundoFastWebApp/Usuario/eliminarUsuario.html', {'usuario': usuario})

def buscarUsuario(request):
    listaUsuario = [usuario for usuario in Usuario.objects.order_by('-id') if request.POST['buscarUsuario'] in usuario.nombreUsuario]
    context = {'listaUsuario': listaUsuario}
    messages.info(request, 'Resultados de búsqueda')
    return render(request, 'MundoFastWebApp/Usuario/usuarios.html', context)