from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# se define el metodo y se le pasa el parametro requests que es proporcionado por django automaticamente
def bienvenido(request):
    # el request contiene la peticion hecha
    return HttpResponse("Wilkommen")