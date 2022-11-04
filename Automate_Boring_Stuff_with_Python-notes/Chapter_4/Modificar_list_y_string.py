print('hola')
l = [34, 46, 97, 'holis']
print(l)
# Se puede asignar valores a multiples variables si
# se ordenan de la siguiente forma

casa = ['perro', 'Patio', 'piscina', 'dos']
baños, salida, lujos, pisos = casa

print('mascotas ' + str(baños))
print('cosas de exterior ' + str(salida))
print('Lujos ' + str(lujos))
print('pisos ' + str(pisos))

# abreviacion de codigos
# para hacer incrementos x veces
spam = 1
spam += 1

# para hacer decrecimientos de x veces
spam -= 1

# para hacer multiplicaciones de por x valor
spam *= 2

# para hacer divisiones entre x valor
spam /= 1

# averiguar para que sirve spam%=1

# Buscar posicion de un elemento en una lista
# se utiliza el comando .index
l.index(34)

# si el elemento no existe en la lista el programa dara un error
# para esto programar un modulo e introducir el buscador para evitar
# que el programa se detenga


# Añadir elementos a una lista

# añadir elementos al final de la lista se utiliza .append

l.append('perro')
print(l)

# Insertar valor en cierta posicion .insert(posicion a ser insertado, elemento a insertar)

import math

a = math.pi
l.insert(2, a)
print(l)

# Remover un elemento segun su valor si no esta definido dara error
l.remove('holis')

# organizar por orden alfabetico listas que solo poseen str .sort()
# este metodo organiza primero en orden alfabetico las letras en
# mayuscula y luego en orden alfabetico las letras en minuscula
# y para recorrer en retroceso el orden se utiliza .sort(reverse=True)
casa.sort()
print(casa)

# tambien puede emplearse para organizar numeros de mayor a menor
# y viseversa esta funcion solo organiza letras o numeros por separado

n = [3, 65, 30, 436, 32]
n.sort(reverse=True)
print(n)

# Si se requiere organizar listas donde se tomen en cuenta solo la letra
# ya sea en mayuscula o minuscula se utiliza 
casa.sort(key=str.lower)
print(casa)

# Reescribir cadenas
# para hacer esto se debe colocar 
# cadenaprincipal[posicion inicial:cantidad de elementos que se desean tomar]
# anticipado o seguido de un + para añadir lo que se desea añadir a la cadena

name = 'Gato a perro'
newname = name[0:5] + 'el ' + name[7:12]
print(newname)

# Tuplas
# a diferencia de las listas estas son inmutables es decir no se
# pueden modificar sus valores
t = (23, 4, 5)

# Una tupla puede ser convertida en lista y viceversa de la siguiente forma
A = list(t)
B = tuple(casa)
print(A)
print(B)

# ultima pagina leida 125
