# Modulo logging 
# con este modulo se puede verificar que ocurre con cada variable, y en que
# orden se ejecuta el mismo, dando una actualizacion de cada elemento
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
# estructura basica del logging este mostrara la fecha de ejecucion, el nivel ejecutado y el mensaje a mostrar def por el programador
logging.debug('Inicio')
N = int(input())


# Funcion factorial
def factorial(n):
    logging.debug('Inicio del factorial(%s)' % (n))
    total = 1
    for i in range(n):  # se podria modificar el inicio del range
        total *= i + 1  # si no fuera por el loggin no se puediera localizar el error de forma mas especificada
        logging.debug('con i = ' + str(i) + ', total es ' + str(total))
    return total
    logging.disable(logging.debug)
    logging.debug('Fin del programa')


print(factorial(N))

# el logging permite activarse o desactivarse mas facilmente que un print
# con el .disable(logging.que se desea deactivar)  a partir de este modulo todos los
# logging que pertenezcan al 

# la funcion logging puede mostrar segun el tipo de seguimiento hecho al programa
# este puede ser de tipo:

# .debug(): de bajo nivel y para detalles pequeños

# .info(): permite recolectar informacion a cerca de que eventos ocurren en el programa
#  y ver como trabajan las cosas en determinados puntos

# .warning() usado para indicar los potenciales problemas que no se preveen en el programa
# pero que podrian afectar a futuro

# .error() usado para registrar un error causante de que el programa falle

# .critical() es de alto nivel y permite identificar un error fatal el cual causa
# que el programa se detenga por completo

# cada una de estas funciones se le puede definir un mensaje a mostrar cuando cada
# una de ella sean definidas

# el logging puede ser escrito en un txt a parte para no saturar de informacion la pantalla
# esto se puede definiendolo de la siguiente manera

logging.basicConfig(filename='log_program.txt', level=logging.DEBUG, format='%(asctime)s\/%(levelname)s\/%(message)s')
# definiendo un archivo a generar y lo que deseamos que dicho archivo contenga
