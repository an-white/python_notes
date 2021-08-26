from django.shortcuts import render

# Create your views here.

def nombre(request):
    container={
        "nombre":"Juan",
        "apellido":"Perez",
        "telefono":"+58-412-111-2222",
        "valor_4":"4",
    }
    return render(request,"nombre.html", container)

def apellido(request):
    container={
        "nombre":"Juan",
        "apellido":"Perez",
        "telefono":"+58-412-111-2222",
        "valor_4":"4",
    }
    return render(request,"apellido.html", container)

def telefono(request):
    container={
        "nombre":"Juan",
        "apellido":"Perez",
        "telefono":"+58-412-111-2222",
        "valor_4":"4",
    }
    return render(request,"telefono.html", container)