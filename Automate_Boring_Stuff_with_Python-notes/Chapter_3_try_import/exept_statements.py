"""
para errores logicos en el programa se utiliza el exept
el cual viene acompañado por la condicion de error
que se desea evitar
"""

def spam(division):
    try:
        return 42 / division
    except ZeroDivisionError:
        print('Error: no se puede dividir entre 0')


"""
si el codigo try causa un error este automaticamente pasara a
la condicion except esta dara el mensaje de error sin provocar
que el programa se detenga en su ejecucion y marcando
un error en ese lugar
"""
print(spam(2))
print(spam(0))
print(spam(12))
print(spam(42))

"""
Al definir try fuera de la funcion este probara cada valor
asignado pero al llegar al error no regresara a la funcion
sin probar el resto de valores asignables a la funcion
"""
print('rotura de try')


def spam(division):
    return 42 / division


try:
    print(spam(2))
    print(spam(0))
    print(spam(12))
    print(spam(42))
except ZeroDivisionError:
    print('Error: no se puede dividir entre 0')
