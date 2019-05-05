from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Producto


def index(request):
    return render(request, 'MundoFastWebApp/index.html')

def productos(request):
    listaProducto = Producto.objects.order_by('-codigoProducto')
    context = {'listaProducto': listaProducto}
    return render(request, 'MundoFastWebApp/productos.html', context)

def verProducto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    return render(request, 'MundoFastWebApp/verProducto.html', {'producto': producto})

def formProducto(request):
    return render(request, 'MundoFastWebApp/crearProducto.html')

def crearProducto(request):
    try:
        producto = Producto(codigoProducto = request.POST['codigoProducto'], nombreProducto = request.POST['nombreProducto'], 
            descripcionProducto = request.POST['descripcionProducto'], categoriaProducto = request.POST['categoriaProducto'], 
            precioProducto = request.POST['precioProducto'],cantidadProducto = request.POST['cantidadProducto'],
            ofertaProducto = request.POST['ofertaProducto'],descuentoProducto = request.POST['descuentoProducto'])
    except (KeyError, Producto.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'MundoFastWebApp/crearProducto.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        producto.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('MundoFastWebApp:productos'))
