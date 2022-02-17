"""
cada variable apunta a una dir de memoria unica que se le asigna una literal
la cual almacena el valor de dicha variable y se reasigna cada vez que se ejecuta el programa
con la funcion id podemos ver dicha posicion de memoria
"""

# agregar un hint para indicar el tipo de variable a esperar aunque se le puede asignar cualquier otro tipo de dato
x: int = 2
print(x)

# otra forma de concatenar strings
test = "test ""1 ""de ""2"

print(test)

# dentro del input podemos escribir un str para indicar que se espera introducion de datos

# f literal en python para imprimir variables es la recomendada a utilizar para imprimir variables
print(f"immmprimmiemmmdo {test}")

# residuo de la division con el operador modulo %

res = 3 % 2
print(f"residuo de la division {res}")

a = True
# not retorna el inverso de la condicion de entrada el operador not es un operador unario es decir solo necesita 1 valor para operar
result = not a
print(result)

# el condicional if se puede def
a = None
if a:  # esto solo verifiacara si la var es != de None del resto si imprime
    print(a)
else:
    print(a)

# operador ternario para condicion if else
# permite ejecutar un condicional en 1 sola linea de codigo pero recomendable si solo se ejecutara 1 linea de codigo para poder leerlo facilmente
a = False
print(f"condicion a es: {a}") if a == True else print(f"condicion a es: {a}")

# los ciclos for y while se puede complementar con un condicional else cuando finalice su ejecucion
for n in range(3):
    # para modificar la terminacion de la linea de impresion se añade el parametro end="terminacion" en la funcion print
    print(n, end=", ")
else:
    print(f"fin del ciclo con n={n}\n")
