# importacion de modulos y funciones predeterminadas
# estas deben ser importadas al inicio del programa 

"""
Modulo random, se le debe definir un intervalo en el cual
se de sea que se generen numeros aleatorios, estos intervalos deben ser def
de menor a mayor. Estos numeros aleatorios son enteros
"""
import math
import random
import sys

for i in range(4):
    print(random.randint(2, 30))

print('introduzca un valor pra el angulo')
x = float(input())
cos = math.cos(x)

print('El cos de ' + str(x) + '=' + str(cos))

"""
con math. se importan funciones matematicas predefinidas en el lenguaje
tales como el numero pi, e, y funciones trigonometricas estas ultimas
calculan en RAD
"""


def hello():
    print('Hola User')
    print('Mi nombre es IA 032120')
    print('Cual es el tuyo?')


"""
con def se definirá una funcion la cual se puede llamar
en cualquier momento en el programa, esta puere realizar
tareas secundarias y permitir reducir el codigo
"""

hello()

# La funcion generada puede depender de variables establecidas previamente en el programa
print('Itroduce tu User name')
name = input()


def hola(name):
    global cos
    print('hola ' + name + str(cos))


"""
Y combinar mensajes de una con otra o generar valores de retorno que
tal vez no tengan relacion con los de entrada al utilizar y modificar
el valor inicial de la variable de entrada esto se realiza
a travez de la palabra return, las variables dentro de
una def son locales y pierden el valor al programa salir de
la funcion, si se desea utilizar una variable global se establece 
global antes de la variable a utilizar y
se modifica el valor asignado
"""

hola(name)

# el rango en reversa se define el inicio del ciclo el fin del ciclo y el paso
start = 3
end = 2
for n in range(start, end, -1):
    print(n)

while True:
    print('escriba exit para salir')
    x = input()
    if x == 'exit':
        print('Gracias por probarnos c:')
        sys.exit()

# sys.exit() permite salir de un programa completamente
