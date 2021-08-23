#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SAP.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# para iniciar el proyecto en django se utliza la siguiente linea
# django-admin startproject "Nombre del proyecto"

# para levantar el proyecto ejecutar la linea
# python manage.py runserver

# esto permite levantar el servicio

# para crear una nueva app se ejecuta la siguiente linea
# django-admin startapp webapp
# para añadir vistas ase debe trabajar dentro del archivo views de la app creada