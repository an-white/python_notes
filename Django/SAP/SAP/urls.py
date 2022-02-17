"""SAP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# importar include para añadir urls de las aplicaciones al proyecto principal
from django.urls import include
from django.urls import path
# importar los metodos para poder acceder a las views
from webapp.views import bienvenido, dinamico, test, consulta

urlpatterns = [
    path('admin/', admin.site.urls),
    # definir el mapeo de urls aqui se añaden las urls que se desean trabajar
    # se definen como funciones
    path('bienvenido', bienvenido),
    path("test", test),
    path("", dinamico),

    # integrar informacion que se va a objetener de nuestra clase de modelo
    path("consulta", consulta),

    # agregar lista urls de una app
    path("personas/", include("personas.urls"))

]
