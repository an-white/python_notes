# Modulo zipfile
"""
permite la compresion, descompresion y lectura de archivos en formatos .zip
pero no permite trabajar con .rar
"""
import zipfile

"""
crear archivos zip
es parecido al generar cualquiero otro archivo con os y abrirlo en modo write
"""
new_zip = zipfile.ZipFile('prueba.zip', 'w')  # permite precargar la opcion de escribir

# añadir elementos al .zip con el modulo write de os
new_zip.write('elementos.txt',
              compress_type=zipfile.ZIP_DEFLATED)
# este tipo de compresion traba con cualquier tipo de datos sin generar problemas

# asignar una variable a un .zip
prueba = zipfile.ZipFile('prueba.zip')
# ver los elementos que este contiene
print(prueba.namelist())

info = prueba.getinfo('elementos.txt')
# tamaño real del archivo seleccionado del .zip
print(info.file_size)
# tamaño del .zip
print(info.compress_size)

# Extraer elementos
prueba.extract('elementos.txt')

# extraer todo el contenido de un .zip
prueba.extractall()
