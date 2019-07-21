from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from .models import Usuario, Producto, Venta, DetalleVenta, Empresa # Importa el modelo
from django.http import Http404 # Importa vista de error 404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
import datetime
from django.contrib import messages # Librería para mensajes
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    return render(request, 'MundoFastWebApp/index.html', {'productoX': Producto})

@login_required
def productos(request):
    listaProducto = Producto.objects.order_by('-id')
    context = {'listaProducto': listaProducto, 'productoX': Producto}
    return render(request, 'MundoFastWebApp/Producto/productos.html', context)

@login_required
def verProducto(request, id):
    productoX = Producto()
    producto = get_object_or_404(Producto, pk=id)
    return render(request, 'MundoFastWebApp/Producto/verProducto.html', {'producto': producto, 'productoX': producto})

@login_required
def formProducto(request):
    producto = Producto()
    return render(request, 'MundoFastWebApp/Producto/crearProducto.html',  {'producto': producto, 'productoX': producto})

@login_required
def crearProducto(request):
    codigo = request.POST['codigoProducto']
    try:
        Producto.objects.get(codigoProducto = int(codigo))
        producto = Producto()
        messages.error(request, 'El código "' + codigo + '" ya pertenece a otro producto.')
        return render(request, "MundoFastWebApp/Producto/crearProducto.html",  {'producto': producto, 'productoX': producto})
    except:
        try:
            producto = Producto(codigoProducto = request.POST['codigoProducto'], nombreProducto = request.POST['nombreProducto'], 
                descripcionProducto = request.POST['descripcionProducto'], categoriaProducto = request.POST['categoriaProducto'], 
                imagenProducto = request.FILES['imagenProducto'], precioProducto = request.POST['precioProducto'],cantidadProducto = request.POST['cantidadProducto'],
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

@login_required
def modificarProducto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        producto.codigoProducto = request.POST['codigoProducto']
        producto.nombreProducto = request.POST['nombreProducto']
        producto.descripcionProducto = request.POST['descripcionProducto']
        try:
            producto.imagenProducto = request.FILES['imagenProducto']
        except:
            pass
        producto.categoriaProducto = request.POST['categoriaProducto']
        producto.precioProducto = request.POST['precioProducto']
        producto.cantidadProducto = request.POST['cantidadProducto']
        producto.ofertaProducto = request.POST['ofertaDropDown']
        producto.descuentoProducto = request.POST['descuentoProducto']
        producto.save()
        messages.success(request, 'Producto modificado correctamente.')
        return HttpResponseRedirect(reverse('MundoFastWebApp:productos'))
    else:
        return render(request, 'MundoFastWebApp/Producto/modificarProducto.html', {'producto': producto, 'productoX': producto})

@login_required
def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        producto.delete()
        messages.error(request, 'Producto eliminado correctamente.')
        return HttpResponseRedirect(reverse('MundoFastWebApp:productos'))
    else:
        return render(request, 'MundoFastWebApp/Producto/eliminarProducto.html', {'producto': producto, 'productoX': producto})

@login_required
def ofertaProducto(request):
    listaProducto = [producto for producto in Producto.objects.order_by('-id') if producto.ofertaProducto]
    context = {'listaProducto': listaProducto, 'productoX': Producto}
    return render(request, 'MundoFastWebApp/Producto/ofertaProducto.html', context)

@login_required
def buscarProducto(request):
    listaProducto = [producto for producto in Producto.objects.order_by('-id') if request.POST['buscarProducto'] in producto.nombreProducto]
    context = {'listaProducto': listaProducto, 'productoX': Producto}
    messages.info(request, 'Resultados de búsqueda.')
    return render(request, 'MundoFastWebApp/Producto/productos.html', context)

@login_required 
def usuarios(request):
    listaUsuario = Usuario.objects.order_by('-rutUsuario')
    context = {'listaUsuario': listaUsuario, 'productoX': Producto}
    return render(request, 'MundoFastWebApp/Usuario/usuarios.html', context)

@login_required
def verUsuario(request, id):
    try:
        usuario = Usuario.objects.get(pk=id)
    except Usuario.DoesNotExist:
        raise Http404("Error. Usuario no existe.")
    return render(request, 'MundoFastWebApp/Usuario/verUsuario.html', {'usuario': usuario, 'productoX': Producto})

@login_required
def formUsuario(request):
    usuario = Usuario()
    return render(request, 'MundoFastWebApp/Usuario/crearUsuario.html', {'usuario': usuario,  'productoX': Producto})

@login_required
def crearUsuario(request):
    try:
        usuario = Usuario.objects.create_superuser(rutUsuario = request.POST['rutUsuario'], nombreUsuario = request.POST['nombreUsuario'], imagenUsuario = request.FILES['imagenUsuario'], rolUsuario = request.POST['rolUsuario'], emailUsuario = request.POST['emailUsuario'], password = request.POST['password'])
    except (KeyError, Usuario.DoesNotExist):
        return render(request, 'MundoFastWebApp/Usuario/crearUsuario.html', {'usuario': usuario, 'error_message': 'Error al crear Nuevo Usuario', 'productoX': Producto})
    else:
        usuario.save()
        messages.success(request, 'Usuario creado correctamente.')
        return HttpResponseRedirect(reverse('MundoFastWebApp:usuarios'))

@login_required
def modificarUsuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    if request.method == 'POST':
        usuario.rutUsuario = request.POST['rutUsuario']
        usuario.nombreUsuario = request.POST['nombreUsuario']
        try:
            usuario.imagenUsuario = request.FILES['imagenUsuario']
        except: 
            pass
        usuario.rolUsuario = request.POST['rolUsuario']
        usuario.emailUsuario = request.POST['emailUsuario']
        if(request.POST['password']!=""):
            usuario.set_password(request.POST['password'])
        usuario.save()
        update_session_auth_hash(request, usuario)
        messages.success(request, 'Usuario modificado correctamente.')
        return HttpResponseRedirect(reverse('MundoFastWebApp:usuarios'))
    else:
        return render(request, 'MundoFastWebApp/Usuario/modificarUsuario.html', {'usuario': usuario, 'productoX': Producto})

@login_required
def eliminarUsuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    if request.method == 'POST':
        usuario.delete()
        messages.error(request, 'Usuario eliminado correctamente.')
        return HttpResponseRedirect(reverse('MundoFastWebApp:usuarios'))
    else:
        return render(request, 'MundoFastWebApp/Usuario/eliminarUsuario.html', {'usuario': usuario, 'productoX': Producto})

@login_required
def buscarUsuario(request):
    listaUsuario = [usuario for usuario in Usuario.objects.order_by('-id') if request.POST['buscarUsuario'] in usuario.nombreUsuario]
    context = {'listaUsuario': listaUsuario, 'productoX': Producto}
    messages.info(request, 'Resultados de búsqueda.')
    return render(request, 'MundoFastWebApp/Usuario/usuarios.html', context)

def iniciarSesión(request, email):
    usuario = get_object_or_404(Usuario, eliminarUsuario = email)
    if request.method == 'POST':
        usuario.emailUsuario = request.POST['emailUsuario']
        usuario.password = request.POST['password']
        return HttpResponseRedirect(reverse('MundoFastWebApp:index', {'productoX': Producto}))
    else:
        return render(request, 'MundoFastWebApp/login/', {'usuario': usuario, 'productoX': Producto})

@login_required
def ventas(request):
    listaVenta = Venta.objects.order_by('-id')
    context = {'listaVenta': listaVenta, 'productoX': Producto}
    return render(request, 'MundoFastWebApp/Venta/ventas.html', context)

@login_required
def formVenta(request):
    venta = Venta()
    listaUsuario = Usuario.objects.order_by('-id')
    listaProducto = Producto.objects.order_by('-id')
    return render(request, 'MundoFastWebApp/Venta/crearVenta.html',
            {'venta': venta, 
             'listaUsuario': listaUsuario,
             'listaProducto': listaProducto, 
             'productoX': Producto})

@login_required
def crearVenta(request):
    try:
        cantProductosVenta = int(request.POST['contProductosVenta'])
        venta = Venta(folioVenta = request.POST['folioVenta'], cuotasVenta = request.POST['cuotasVenta'], subTotal = request.POST.get('subTotal'), 
            descuendoAdicionalVenta = request.POST['descuentoAdicionalVenta'], totalVenta = request.POST.get('totalVenta'),
            estadoVenta = request.POST['estadoVenta'], responsableVenta = Usuario.objects.get(emailUsuario = request.POST['responsableVenta']))
        venta.save()
        for i in range(cantProductosVenta):
            productoAux = Producto()
            productoAux = Producto.objects.get(codigoProducto=request.POST.get('codigoProductoVenta'+str(i)))
            cantidadProductoVenta = request.POST.get('cantidadProductoVenta'+str(i))
            productoAux.cantidadProducto -= int(cantidadProductoVenta)
            if productoAux.cantidadProducto < 0:
                productoAux.cantidadProducto += int(cantidadProductoVenta)
                venta.delete()
                venta = Venta()
                listaUsuario = Usuario.objects.order_by('-id')
                listaProducto = Producto.objects.order_by('-id')
                context = {
                    'venta': venta,
                    'listaUsuario': listaUsuario,
                    'listaProducto': listaProducto
                }
                messages.error(request, 'Stock de %s es %s' %(productoAux.nombreProducto, productoAux.cantidadProducto))
                return render(request, "MundoFastWebApp/Venta/crearVenta.html", context)
            else:
                totalProducto = productoAux.precioProducto - (productoAux.precioProducto * productoAux.descuentoProducto / 100)
                detalleVenta = DetalleVenta(producto=productoAux, venta=venta, cantidadProducto=cantidadProductoVenta, descuentoAplicadoProducto=productoAux.descuentoProducto, totalPorProducto=totalProducto)
                detalleVenta.save()
                productoAux.save()
    except IntegrityError:
        return render(request, "MundoFastWebApp/Venta/crearVenta.html", {"error_message": "Dejaste un campo vacío", 'productoX': Producto})
    else:
        messages.success(request, 'Venta creada correctamente.')
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('MundoFastWebApp:ventas'))
        

@login_required
def buscarVenta(request):
    alt = request.POST['buscarVenta']
    if request.POST['buscarVenta']:
        listaVenta = [x for x in Venta.objects.order_by('-id') if int(alt) == x.folioVenta]
        context = {'listaVenta': listaVenta, 'productoX': Producto}
        messages.info(request, 'Resultados de búsqueda.')
        return render(request, 'MundoFastWebApp/Venta/ventas.html', context)
    else:
        return HttpResponseRedirect(reverse('MundoFastWebApp:ventas'))

@login_required
def verVenta(request, id):
    venta = get_object_or_404(Venta, pk=id)
    listaDetalleVenta = [detalleVenta for detalleVenta in DetalleVenta.objects.order_by('-id') if venta.id == detalleVenta.venta.id]
    return render(request, 'MundoFastWebApp/Venta/verVenta.html', {'venta': venta, 'listaDetalleVenta': listaDetalleVenta, 'productoX': Producto})

@login_required
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
            return render(request, "MundoFastWebApp/Venta/modificarVenta.html", {"error_message": "Error de integridad", 'productoX': Producto})
        else:
            messages.success(request, 'Venta modificada correctamente.')
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('MundoFastWebApp:ventas'))
    else:
        return render(request, 'MundoFastWebApp/Venta/modificarVenta.html', {'venta': venta, 'listaProducto':listaProducto, 'listaDetalleVenta': listaDetalleVenta, 'listaUsuario': listaUsuario, 'productoX': Producto})

@login_required
def eliminarVenta(request, id):
    venta = get_object_or_404(Venta, pk=id)
    listaDetalleVenta = [detalleVenta for detalleVenta in DetalleVenta.objects.order_by('-id') if venta.id == detalleVenta.venta.id]
    if request.method == 'POST':
        venta.delete()
        messages.error(request, 'Venta eliminada correctamente.')
        return HttpResponseRedirect(reverse('MundoFastWebApp:ventas'))
    else:
        return render(request, 'MundoFastWebApp/Venta/eliminarVenta.html', {'venta': venta, 'listaDetalleVenta': listaDetalleVenta, 'productoX': Producto})

def verPerfilEmpresa(request):
    try:
        empresa = Empresa.objects.get(pk=1)
    except Empresa.DoesNotExist:
        raise Http404("Error. URL no válido.")
    return render(request, 'MundoFastWebApp/Empresa/verPerfilEmpresa.html', {'empresa': empresa, 'productoX': Producto})

@login_required
def modificarPerfilEmpresa(request):
    empresa = get_object_or_404(Empresa, pk=1)
    if request.method == 'POST':
        empresa.nombreEmpresa = request.POST['nombreEmpresa']
        empresa.emailEmpresa = request.POST['emailEmpresa']
        empresa.descripcionEmpresa = request.POST['descripcionEmpresa']
        empresa.direccionEmpresa = request.POST['direccionEmpresa']
        empresa.horarioEmpresa = request.POST['horarioEmpresa']
        empresa.imagenEmpresa = request.POST['imagenEmpresa']
        empresa.save()
        messages.success(request, 'Información de Empresa modificada correctamente.')
        return HttpResponseRedirect(reverse('MundoFastWebApp:verPerfilEmpresa'))
    else:
        return render(request, 'MundoFastWebApp/Empresa/modificarPerfilEmpresa.html', {'empresa': empresa, 'productoX': Producto})

@login_required
def reportes(request):
    return render(request, 'MundoFastWebApp/Reporte/reportes.html', {'productoX': Producto})

@login_required
def reporteDiario(request):
    try:
        listaVenta = [venta for venta in Venta.objects.order_by('-id') if venta.fechaVenta.date() == datetime.date.today()]
    except TypeError:
        return render(request, 'MundoFastWebApp/Reporte/reportes.html')
    context = {'listaVenta': listaVenta, 'productoX': Producto}
    return render(request, 'MundoFastWebApp/Reporte/reporteDiario.html', context)

@login_required
def reporteMensual(request):
    try:
        listaVenta = [venta for venta in Venta.objects.order_by('-id') if venta.fechaVenta.month == datetime.date.today().month and venta.fechaVenta.year == datetime.date.today().year]
    except TypeError:
        return render(request, 'MundoFastWebApp/Reporte/reportes.html')
    context = {'listaVenta': listaVenta, 'productoX': Producto}
    return render(request, 'MundoFastWebApp/Reporte/reporteMensual.html', context)

@login_required
def reporteAnual(request):
    try:
        listaVenta = [venta for venta in Venta.objects.order_by('-id') if venta.fechaVenta.year == datetime.date.today().year]
    except TypeError:
        return render(request, 'MundoFastWebApp/Reporte/reportes.html')
    context = {'listaVenta': listaVenta, 'productoX': Producto}
    return render(request, 'MundoFastWebApp/Reporte/reporteAnual.html', context)

@login_required
def reportePersonalizado(request):
    try:
        listaVenta = [venta for venta in Venta.objects.order_by('-id') if request.POST['fechaInicio']<= str(venta.fechaVenta.date()) <= request.POST['fechaTermino']]
    except TypeError:
        return render(request, 'MundoFastWebApp/Reporte/reportes.html')
    fechaInicio = request.POST['fechaInicio']
    fechaTermino = request.POST['fechaTermino'] 
    context = {'listaVenta': listaVenta, 'fechaInicio': fechaInicio, 'fechaTermino': fechaTermino, 'productoX': Producto}
    return render(request, 'MundoFastWebApp/Reporte/reportePersonalizado.html', context)

# TEMPORALES

def verCatalogo(request):
    categoria = request.POST['categoriaProducto']
    nombreProductoBusqueda = request.POST['sbNombreProducto']
    if categoria == "Todas las categorías" and nombreProductoBusqueda == "":
        listaProducto = Producto.objects.all()
    elif nombreProductoBusqueda != "" and categoria == "Todas las categorías":
        listaProducto = [producto for producto in Producto.objects.all() if nombreProductoBusqueda in producto.nombreProducto]
    elif categoria != "Todas las categorías" and nombreProductoBusqueda == "":
        listaProducto = [producto for producto in Producto.objects.all() if producto.categoriaProducto == categoria]
    else:
        listaProducto = [producto for producto in Producto.objects.all() if nombreProductoBusqueda in producto.nombreProducto and producto.categoriaProducto == categoria]
    context = {
        'listaProducto': listaProducto,
        'productoX': Producto
    }
    return render(request, 'MundoFastWebApp/Catalogo/verCatalogo.html', context)

def verProductoCatalogo(request, id):
    producto = get_object_or_404(Producto, pk=id)
    return render(request, 'MundoFastWebApp/Catalogo/verProductoCatalogo.html', {'producto': producto, 'productoX': Producto})

def verOfertas(request):
    listaProductoOferta = [producto for producto in Producto.objects.order_by('id') if bool(producto.ofertaProducto)]
    listaPrecioDescontado = []
    for producto in Producto.objects.order_by('id'):
        if bool(producto.ofertaProducto):
            descuento = int(producto.precioProducto) - (int(producto.precioProducto) * (int(producto.descuentoProducto)/100))
            listaPrecioDescontado.append(int(descuento))
    lista = tuple(zip(listaProductoOferta, listaPrecioDescontado))
    context = {
        'lista': lista,
        'productoX': Producto
    }
    return render(request, 'MundoFastWebApp/Catalogo/verCatalogoOferta.html', context)

def contactoEmpresa(request):
    if(Empresa.DoesNotExist):
        empresa = Empresa.objects.get_or_create(nombreEmpresa="Mundo Fast SPA", emailEmpresa="mundofaststore@gmail.com", direccionEmpresa = "Super Agro Santa María - Local X", descripcionEmpresa = "Descripción", horarioEmpresa = "Todos los días", imagenEmpresa="")
        empresa = Empresa.objects.get(pk=1)
    return render(request, 'MundoFastWebApp/Contacto/contactoEmpresa.html', {'empresa': empresa, 'productoX': Producto})

def contactarEmpresa(request):
    try:
        empresa = Empresa.objects.get(pk=1)
        subject = request.POST['asunto']
        from_email = request.POST['remitente']
        message = request.POST['mensaje']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['contactomundofast@gmail.com',]   
        send_mail( subject, 'Remitente: ' + from_email + '\n' + message, email_from, recipient_list )
    except IntegrityError:
        return render(request, "MundoFastWebApp/Contacto/contactoEmpresa.html", {'empresa': empresa, 'productoX': Producto})
    return render(request, 'MundoFastWebApp/Contacto/contactoRealizado.html', {'productoX': Producto})
