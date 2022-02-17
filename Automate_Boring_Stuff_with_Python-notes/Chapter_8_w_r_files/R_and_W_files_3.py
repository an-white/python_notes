# read files

Emails = open('C:\\Users\\andre\\Desktop\\Analizados con Python.txt', 'r')
"""
esta estructura nos cargara el modo lectura, esta carga actualmente por def en python
si genera error en la lectura se debe def el tipo de encoding a leer,
en mi caso 'Latin-1' 
tambien para todos los idiomas el 'UTF-8'
debe def una estructura para encoding en caso de existir errores y que
el programa continue su ejecucion
"""

print(Emails)

# para ver el texto del .txt se usa 
txt = Emails.read()  # genera un str debe
print(txt)

"""
si se desea generar una list con cada una de las lineas del doc analizado
se utiliza .readlines()
"""

task = open('C:\\Users\\andre\\Desktop\\Task.txt')
txt = task.readlines()  # genera una list generando 1 elemento de la list por cada salto de linea del txt
print(txt)

# para escribir o crear un archivo nuevo se utiliza la siguiente estructura
Emails = open('C:\\Users\\andre\\Desktop\\Emails.txt',
              'w')  # con el, 'w' si el .txt seleccinado no existe phyton lo creaara antes de escribir en el
Emails.write('Primer texto a distancia C:\n')
Emails.close()  # para cerrar el archivo

"""
si se desea añadir texto en un archivo ya creado se coloca al lado
del path ,'a'
"""
Emails = open('C:\\Users\\andre\\Desktop\\Emails.txt',
              'a')  # el 'a' añadirá mas texto en la cadena para ir asi llenando el .txt
Emails.write('Asustado Potter\nPara nada Bv')
Emails.close()
# pag 208
