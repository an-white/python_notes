"""
Diccionarios posen keys los cuales permiter obtener los valores asignados
en el mismo, estos a diferencia de las listas no estan ordenados
es decir mientras 2 diccionarios tengan los mismos elementos
sin importar su posicion estos para python seran iguales
"""

cumple = {'Andrea': 'Apr 2', 'Santiago': 'Dic 7', 'Andres': 'Sep 7'}

while True:
    print('Introduce tu nombre para ver tu fecha de cumpleaños, dejar vacio para salir')
    name = input()
    if name == '':
        break

    if name in cumple:
        print(cumple[name] + ' es el cumpleaños de ' + name)
    else:
        print('No lo poseo a ' + name + ' en mi base de datos')
        print('Cual es la fecha de su cumpleaños')
        dia = input()
        cumple[name] = dia  # esto añadira un elemento al directorio,
        # siendo [name la key asignada]= dia el valor asignado a la nueva key 
        print('La base de datos ha sido actualizada con exito!')

"""
para poder ver todos los elementos diccionario se utiliza .values()
dentro de un ciclo for de la siguiente manera:
"""
Dictionary = {'alfa': 1, 'beta': 2, 'gamma': 3, 'omega': 5}
for v in Dictionary.values():
    print(v)

"""
Para poder ver todos los nombres de las key de un diccionario se emplea
.keys() dentro de un ciclo for
"""
for k in Dictionary.keys():
    print(k)

"""
de igual manera se puede generar una list a partir de las keys 
o values de las mismas de la siguiente forma
"""

A = list(Dictionary.values())
B = list(Dictionary.keys())
print('Valores de las Keys \n ' + str(A))
print('Nombres de las Keys \n ' + str(B))

"""
para ver todos los items dentro de un diccionario se utiliza .items()
esto mostrara en forma de par ordenado todos los items ordenando
(key,valor de key)
"""

for i in Dictionary.items():
    print(i)

"""
Se puede chequear la existencia de una key o value key en un
diccionario de igual manera que en una list se chequeaba la 
existencia de un elemento con las condiciones in, not in
"""
print('alfa' in Dictionary.keys())

"""una forma mas sencilla de verificar la existencia de una key 
y su valor asignado se puede utilizar el metodo
 .get('key buscada', valor en caso de no estar contenido en el diccionario)
"""

print('Que valor de key desea buscar')
k = input()
print(
    'Existe un ' + k + ' el cual tiene un valor asignado de ' + str(Dictionary.get('"' + str(k) + '"', 'No contenido')))

print('Existe un alfa el cual tiene un valor asignado de ' + str(Dictionary.get('alfa', 0)))

"""
para añadir un elemento de manera corta a un diccionario se emplea
el modulo .setdefault() el cual permite añadir (key, valor de key)
Pero este no permitira reescribir una variable existente dentro del diccionario
"""

Dictionary.setdefault('Lambda', 3)
print(Dictionary)

"""
Si se desea contar la cantidad de veces que un caracter se repite
en una cadena se puede utilizar el .setdefault() y generar un diccionario
con la sigiente estructura
"""
mensaje = 'Hola como estas yo muy bien aprovechando el tiempo de cuarentena y tu?'

contador = {}
for c in mensaje:
    contador.setdefault(c, 0)
    contador[c] = contador[c] + 1
print(contador)
