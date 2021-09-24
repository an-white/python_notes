Nombres=[]
while True:
    print('Introduzca los nombres de los elementos de la lista '+ str(len(Nombres)+1)+' O dejar vacio para terminar la lista')
    name= input()
    if name=='':
        break
    Nombres= Nombres+[name] 
    # al colocar [name] estamos def como un valor añadible a una
    # lista esto permitira añadir cada valor ingresado a nuestra lista sin errores
print('Los nombres en la lista son:')
for name in Nombres:
    print(' '+name)# el espacio antes de name se coloca para dejar una separacion entre el margen de la ventana y el nombre de cada uno
    

# Se puede establecer un ciclo for el cual el rango sea igual a la
# cantidad de elementos que pertenecen a una cierta lista

supplies=['pens', 'paper', 'pencils', 'sticky notes', 'Erasers']
print('\nUtiles escolares en inventario:')
for i in range(len(supplies)):
    print(' Slot '+ str(i+1)+ ': ' + supplies[i])

# Operadores in, and, not in
# se pueden utilizar para ubicar cierto elemento dentro de la lista
# lo que permite la ubicacion de nombres o cifras dentro de la misma

spam = ['hello', 'hi', 'howdy', 'heyas']
print('QUe elemento desea buscar dentro de la lista spam')
buscar = input()

print(buscar in spam)

# Modulo .copy
# El .copy permite hacer una copia es decir 
# esta se puede modificar sin alterar al original 

al=spam.copy()

# Modulo clear vacia la lista

al.clear()