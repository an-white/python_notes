import os

# Modulo .path toda la informacion restante a cerca de este modulo se
# http://docs.phython.org/3/library/os.path.html.

path = 'C:\\Users\\andre\\Desktop'
os.chdir(path)
print(os.getcwd())
path = '.\\andre\Desktop'  # para definir ubicar un dir dentro del dir que actualemnte se esta trabajando

# con .isabs(nombre del dir) puede evaluar si el dir es path es existe o no

print(os.path.isabs(path))

# .path.abspath(nombre parcial del dir) da como resultado el path completo
# si es introducido parcialmente una buena forma de trasnformar path parciales en abs

print(os.path.abspath(path))
# .relpath(path, desde donde queremos visualizar el path parcial que se mostrara)

p_1 = os.path.relpath(path, '\\andre')
p_2 = os.path.relpath(path, 'C:\\')
print(p_1 + '\n' + p_2)

# .path.dirname(path) muestra todo lo que viene antes de el ultimo slash en la
# dir del path , mientras que el .path.basename(path) dara como resultado
# el nombre el archivo que esta asociado al path
path = 'C:\\Users\\andre\\Desktop\\andre.exe'
print('\n' + os.path.dirname(path))
print('\n' + os.path.basename(path) + '\n')

# si se ha de necesitar el path dir y base juntos se recurre al .path.split()
# el cual nos regresara los valores de cada uno en forma de tupla
# (dir, base)

print(os.path.split(path))

# para que el nombre de cada carpeta sea separado en un elemento en una list
# se debe recurir al modulo .split(os.path.sep) el cual separará cada elemento
# que conforma el path

print(path.split(os.path.sep))  # los separadores estaran dados por , entre cada carpeta del path

# obtener el tamaño de un archivo mediante el .path.getsize(path) devolvera
# el tamaño en bits del archivo analizado
path = 'C:\\Users\\andre\\Desktop\\correos.txt'
p_1 = os.path.getsize(path)
print(str(p_1) + ' Bits')

# obtener el nombre de todos los elementos contenidos en un path

p_2 = os.listdir('C:\\Users\\andre\\Desktop')
print('\n')
print(p_2)

# Para obtener el tamaño total de todos elementos contenidos en una carpeta
# se puedee emplear la sig estructura
Total = 0
for archivo in os.listdir('C:\\Users\\andre\\Desktop'):
    Total = Total + os.path.getsize(os.path.join('C:\\Users\\andre\\Desktop', archivo))
print('\n' + str(Total) + ' Bits\n')

# para verificar path de direcciones, archivos y su existencia se usan
# dan como resultado un booleano

path = 'C:\\Users\\andre'
p_1 = os.path.exists(path)  # verifica si el path existe o no
print(p_1)

path = 'C:\\Users\\andre\\Desktop\\correos.txt'
p_2 = os.path.isfile(path)  # Dira si es o no un archivo
print(p_2)

path = 'C:\\Users\\andre\\Desktop'
p_3 = os.path.isdir(path)  # Dira si es o no la direccion de una carpeta
print(p_3)

# con el .exists podemos verificar si un dispositivo usb, o dvd esta 
# actualmente conectado al dispositivo
