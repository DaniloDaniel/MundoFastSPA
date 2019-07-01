from django.shortcuts import get_object_or_404, render, render_to_response
from .models import Usuario, Producto, Venta, DetalleVenta # Importa el modelo
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
    messages.info(request, 'Resultados de búsqueda.')
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
        usuario = Usuario.objects.create_superuser(rutUsuario = request.POST['rutUsuario'], nombreUsuario = request.POST['nombreUsuario'], emailUsuario = request.POST['emailUsuario'], imagenUsuario = request.POST['imagenUsuario'], rolUsuario = request.POST['rolUsuario'], password = request.POST['password'])
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
        usuario.password = request.POST['password']
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
    messages.info(request, 'Resultados de búsqueda.')
    return render(request, 'MundoFastWebApp/Usuario/usuarios.html', context)

def iniciarSesión(request, email):
    usuario = get_object_or_404(Usuario, eliminarUsuario = email)
    if request.method == 'POST':
        usuario.emailUsuario = request.POST['emailUsuario']
        usuario.password = request.POST['password']
        return HttpResponseRedirect(reverse('MundoFastWebApp:index'))
    else:
        return render(request, 'MundoFastWebApp/login/', {'usuario': usuario})
def ventas(request):
    listaVenta = Venta.objects.order_by('-id')
    context = {'listaVenta': listaVenta}
    return render(request, 'MundoFastWebApp/Venta/ventas.html', context)

def formVenta(request):
    venta = Venta()
    listaUsuario = Usuario.objects.order_by('-id')
    listaProducto = Producto.objects.order_by('-id')
    return render(request, 'MundoFastWebApp/Venta/crearVenta.html',
            {'venta': venta, 
             'listaUsuario': listaUsuario,
             'listaProducto': listaProducto})

def crearVenta(request):
    try:
        cantProductosVenta = int(request.POST['contProductosVenta'])
        detallesVenta = []
        venta = Venta(folioVenta = request.POST['folioVenta'], cuotasVenta = request.POST['cuotasVenta'], subTotal = request.POST.get('subTotal'), 
            descuendoAdicionalVenta = request.POST['descuentoAdicionalVenta'], totalVenta = request.POST.get('totalVenta'),
            estadoVenta = request.POST['estadoVenta'], responsableVenta = Usuario.objects.get(emailUsuario = request.POST['responsableVenta']))
        venta.save()
        for i in range(cantProductosVenta):
            productoAux = Producto()
            productoAux = Producto.objects.get(codigoProducto=request.POST.get('codigoProductoVenta'+str(i)))
            cantidadProducto = request.POST.get('cantidadProductoVenta'+str(i))
            totalProducto = productoAux.precioProducto - (productoAux.precioProducto * productoAux.descuentoProducto / 100)
            detalleVenta = DetalleVenta(producto=productoAux, venta=venta, cantidadProducto=cantidadProducto, descuentoAplicadoProducto=productoAux.descuentoProducto, totalPorProducto=totalProducto)
            detalleVenta.save()
    except IntegrityError:
        return render(request, "MundoFastWebApp/Venta/crearVenta.html", {"error_message": "Dejaste un campo vacío"})
    else:
        messages.success(request, 'Venta creada correctamente.')
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('MundoFastWebApp:ventas'))

def buscarVenta(request):
    alt = request.POST['buscarVenta']
    if request.POST['buscarVenta']:
        listaVenta = [x for x in Venta.objects.order_by('-id') if int(alt) == x.folioVenta]
        context = {'listaVenta': listaVenta}
        messages.info(request, 'Resultados de búsqueda.')
        return render(request, 'MundoFastWebApp/Venta/ventas.html', context)
    else:
        return HttpResponseRedirect(reverse('MundoFastWebApp:ventas'))

def verVenta(request, id):
    venta = get_object_or_404(Venta, pk=id)
    listaDetalleVenta = [detalleVenta for detalleVenta in DetalleVenta.objects.order_by('-id') if venta.id == detalleVenta.venta.id]
    return render(request, 'MundoFastWebApp/Venta/verVenta.html', {'venta': venta, 'listaDetalleVenta': listaDetalleVenta})

def modificarVenta(request, id):
    venta = get_object_or_404(Venta, pk=id)
    listaDetalleVenta = [detalleVenta for detalleVenta in DetalleVenta.objects.order_by('-id') if venta.id == detalleVenta.venta.id]
    listaProducto = Producto.objects.order_by('-id')
    listaUsuario = Usuario.objects.order_by('-id')
    if request.method == 'POST':
        try:
            venta.cuotasVenta = request.POST['cuotasVenta']
            venta.subTotal = request.POST['subTotal']
            venta.totalVenta = request.POST['totalVenta']
            venta.estadoVenta = request.POST['estadoVenta']
            venta.responsableVenta = Usuario.objects.get(emailUsuario=request.POST['responsableVenta'])
            venta.descuentoAdicionalVenta = request.POST['descuentoAdicionalVenta']
            venta.save()
        
            cantProductosVenta = int(request.POST['contProductosVenta'])
            detallesVenta = []
            b = DetalleVenta.objects.filter(venta=venta.id)
            b.delete()
            for i in range(cantProductosVenta):
                productoAux = Producto()
                productoAux = Producto.objects.get(codigoProducto=request.POST.get('codigoProductoVenta'+str(i)))
                cantidadProducto = request.POST.get('cantidadProductoVenta'+str(i))
                totalProducto = productoAux.precioProducto - (productoAux.precioProducto * productoAux.descuentoProducto / 100)
                detalleVenta = DetalleVenta(producto=productoAux, venta=venta, cantidadProducto=cantidadProducto, descuentoAplicadoProducto=productoAux.descuentoProducto, totalPorProducto=totalProducto)
                detalleVenta.save()
        except IntegrityError:
            return render(request, "MundoFastWebApp/Venta/modificarVenta.html", {"error_message": "Error de integridad"})
        else:
            messages.success(request, 'Venta modificada correctamente.')
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('MundoFastWebApp:ventas'))
    else:
        return render(request, 'MundoFastWebApp/Venta/modificarVenta.html', {'venta': venta, 'listaProducto':listaProducto, 'listaDetalleVenta': listaDetalleVenta, 'listaUsuario': listaUsuario})

def eliminarVenta(request, id):
    venta = get_object_or_404(Venta, pk=id)
    if request.method == 'POST':
        if 'opcionSi' in request.POST:
            venta.delete()
            messages.error(request, 'Venta eliminado correctamente.')
        return HttpResponseRedirect(reverse('MundoFastWebApp:ventas'))
    else:
        return render(request, 'MundoFastWebApp/Venta/eliminarVenta.html', {'venta': venta})