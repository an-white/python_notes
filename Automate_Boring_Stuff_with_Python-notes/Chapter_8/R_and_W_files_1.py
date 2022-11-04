import os
import pyperclip

# esto nos permite generalizar la entrada de directorios
# Ya que dependiendo del SO la forma en que estos se organizan
# varia segun el sistema utilizado, para lo que podemos utilizar el

dir = os.path.join('C', 'Usuarios', 'Black PC', 'Documentos', 'Universidad')
print(str(dir))
pyperclip.copy(dir)

# el os.path.join colocara los separadores de directorios que 
# correspondan al SO

# con este modulo se puede dar ubicacion a un archivo nuevo que se
# desee introducir en cierto directorio

Archivos = ['cuentas.txt', 'Brochure.ai', 'Photo.psd']
for n_archivo in Archivos:
    print(os.path.join('C', 'Usuarios', 'Black PC', 'Documentos', n_archivo))

# el .getcwd() nos arrojara como resultado al direccion actual del archivo
# que estamos trabajando
print(os.getcwd())

# con el Modulo .chdir() podremos cambiar la actual direccion a la que 
# deseemos reubicar el programa actual

os.chdir('C:\\Users\\andre')  # si el path para reubicar no existe dara un error como resultado

# con .\ se puede dar la ubicacion parcial de un archivo que pertenezca
# a la carpeta que actualmente estamos trabajando

# con ..\ nos permite acceder a un dir que este ubicado en la carpeta raiz
# del SO

# para crear una nueva carpeta se utiliza el si alguna de los dir intermedios
# no existen python los creara hasta poder armar el path proporcionado al modulo

os.makedirs('C:\\Users\\andre\\Desktop\\andre')
