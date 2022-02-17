l = [3, "Amo", "Great", "GG"]

list = [2, l, "arco", True, "Pi", 45]  # lista l contenido en otro vector list
print('\n List')
print(list)

# Invocacion de elementos de listas
E1 = l[3]
E2 = list[2]
print('\n Elementos seleccionados')  # \n es un salto de linea
print(E1 + " " + E2)

"""
Crear una lista a partir de otra
primer numero antes de los : es el inicio de 
la nueva lista el numero despues de : es la posicion del  
ultimo elemento que tomará de la lista inicial
"""

print('\n Vector que toma datos de List')
L2 = list[1:3]
print(L2)

"""
si se desea un salto en la seleccion de elementos se debe
colocar otro : y definir el salto como el salto que 
se desea como cada cuantos elementos queremos tomar uno nuevo
es decir 2 para cada 1 si 1 no y 3 para cada 2 elementos uno nuevo
"""
print('\n Vector que toma datos de List con un salto de seleccion')
l3 = list[1:6:2]
print(l3)

# Reasignar el valor de un elemento en una lista
l[1] = 'Carros'
# El elemento reasignado tambien puede pertenecer a la misma lista u otra lista

"""
Concatenacion de listas
permite la union o repeticion de n veces de una lista loa union
es mediante + y la repeticion mediente *n veces se desee repetir
"""

c = [3, 4, 'alfa', 'omega']
concatenacion = c + l
print('\nLa union de l y c \n' + str(concatenacion) + '\n')

# Eliminar elementos de la lista
del l[0]
print(l)

# Cantidad de elementos en una lista
print('\nCantidad de elementos en l=' + str(len(l)) + '\n')
