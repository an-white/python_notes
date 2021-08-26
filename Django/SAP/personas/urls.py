
from personas.views import nombre, apellido, telefono
from django.urls import path
# importar include para añadir urls de las aplicaciones al proyecto principal

urlpatterns = [
    # definir el mapeo de urls aqui se añaden las urls que se desean trabajar
    # se definen como funciones
    path('nombre/', nombre),
    path("apellido/",apellido),
    path("telefono/",telefono),
    
]   
