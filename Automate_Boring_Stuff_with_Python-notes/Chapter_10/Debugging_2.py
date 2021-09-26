# esta libreria permite ver cual es el error en el programa generando un 
# informe en un txt el cual permite tener el error que detenga el programa
# y permite seguir con la ejecucion del programa 
import traceback

try:
    raise Exception('Error :c')
except:
    error_txt=open('.\error.txt','w')
    error_txt.write(traceback.format_exc())
    error_txt.close()
    print('\nel informe de error fue generado correctamente en el archivo error.txt\n')

print('error saltado')

# Aseveraciones
# son verificaciones de verdadero o falso que permiten dar errores de 
# programas y detener su ejecucion su uso es para errores del programador mas no del usuario
# estas cuentan con: la palabra clave, la condicion que debe o no cumplir, una coma ,
# y una cadena en la cual se debe o no cumplir esta condicion

puerta = 'abierta'
assert puerta=='abierta', 'la puerta esta "abierta"'

txt='hola'
assert txt=='perro', 'hola como "estas"'

# En el primer ejemplo la def se cumple y el programa se continua ejecutando
# mientras que en el 2do la condicion evaluada no se cumple y el programa genera el
# error, y detiene su ejecucion