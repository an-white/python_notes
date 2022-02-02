# para poder hacer renders de templates
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# se define el metodo y se le pasa el parametro requests que es proporcionado por django automaticamente
def bienvenido(request):
    # el request contiene la peticion hecha
    return HttpResponse("Wilkommen")


def test(request):
    # declaracion de renderizado de templates este buscara dentro de la caperta del modulo la carpeta templates el archivo html que le solicitemos
    # se puede def otra url 
    return render(request, "test.html")


# elementos dinamicos en las plantillas

def dinamico(request):
    container = {
        "data": ["valor_1", 1, "valor_2", "2", "valor_3", "3", "valor_4", "4", ],
        "container": [
            {"vehiculo": "Carro", "marca": "Aston Martin"},
            {"vehiculo": "Carro", "marca": "Ferrary"},
            {"vehiculo": "Carro", "marca": "Tesla"},
            {"vehiculo": "Avion", "marca": "Cessna"},
        ]
    }
    return render(request, "dinamico.html", container)


def consulta(request):
    container = {
        "valor_1": "1",
        "valor_2": "2",
        "valor_3": "3",
        "valor_4": "4",
    }
    return render(request, "dinamico.html", container)
