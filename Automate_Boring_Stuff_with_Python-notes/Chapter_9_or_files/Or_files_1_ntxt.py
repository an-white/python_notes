# Modulo shutil 
# este modulo permite copiar, mover y renombrar archivos

import os
import shutil


def Ch_Path():
    shutil.copytree('.\Remover', '.\Remove')
    os.unlink('.\Remove\temp3.txt')
    os.unlink('temp3.txt')


"""
Copiar archivos y carpetas
se def un path de origen y uno de destino


Copiar carpetas
el modulo .copytree permite copiar carpetas y todo su contenido
este comando a su vez permite crear una nueva carpeta contenedora si esta no existe previamente
"""

shutil.copytree('C:\\Users\\Black PC\\Documents\\Proyects', 'C:\\Users\\Black PC\\Desktop\\prueba\\Proyectosky')

# Copiar archivos
shutil.copy('C:\\Users\\Black PC\\Desktop\Emails_Hunter.py', 'C:\\Users\\Black PC\\Desktop\\prueba\\Emails.py')

"""
Mover y renombrar archivos y carpetas
para mover un archivo o carperta se utiliza el modulo .move(carpeta de origen, carpeta de destino)
la carpeta debe existir
"""
shutil.move('C:\\Users\\Black PC\\Desktop\\prueba\\Asignación de Ingles-Andres Blanca.pdf',
            'C:\\Users\\Black PC\\Desktop\\Asignación.pdf')

"""
Si existe un archivo con el mismo nombre el programa lo reescribira automaticamente
Con este modulo tambien es posible renombrar los archivos al reubicarlos
Al añadir el nombre que se desea colocar el la archivo en el path de destino
el programa interpreta primero la reubicacion y luego renombra el archivo
"""
for i in range(3):
    t = 'temp%s.txt' % (i + 1)
    path = os.path.join(t)
    dir = open(path, 'w')

print('pausa 1')
p = input()

# Moviendo y cambiando el nombre de un archivo
shutil.move('temp1.txt', 'C:\\Users\\Black PC\\Desktop\\prueba\change_1.txt')

shutil.move('C:\\Users\\Black PC\\Desktop\\Asignación.pdf',
            'C:\\Users\\Black PC\\Desktop\\prueba\\Asignación de Ingles-Andres Blanca.pdf')

"""
se debe especificar correctamente la direccion de destino si no dara un error
eliminar archivos
"""
os.unlink('temp2.txt')

# Eliminar carptas y su contenido shutil.rmtree(path)
shutil.rmtree('C:\\Users\\Black PC\\Desktop\\prueba\\Proyectosky')

print('pausa 2')
input()
Ch_Path()

# Eliminar carpetas vacias os.redir(path)
os.rmdir('.\Remove')
