import os
import shelve

# este modulo permite recuperar datos que guarden las variables
# en el disco duro, esto permite guardar configuraciones y registros
# de un programa
os.chdir('.\Chapter_8')
Config = shelve.open('Data')
# al abrir el modulo permite escribir los archivos data si estos no existen
# si existen los permitira leer a continuacion

letter = ['alfa', 'beta', 'gamma', 'delta']
Config['letter'] = letter
# esto permite asignar una key a Data el cual almacenara los valores
# de nuestras variables
Config.close()  # cierra el modulo de config

# se puede guardar una config con pprint, generando otro archivo .py,
# este archivo es generado mediante el modulo pprint, siendo una
# forma mas sencilla de ver los elementos contenidos en esta base de datos
# pero un poco mas trabajosa de armar

import pprint

letter = [{'letra': 'alfa', 'pos': '1'}, {'letra': 'beta', 'pos': '2'}, {'letra': 'gamma', 'pos': '3'},
          {'letra': 'delta', 'pos': '4'}]
Doc = open('Data.py', 'w')  # generarmos archivo .py
Doc.write('Letras_griegas=' + pprint.pformat(letter))

# las str a escribir no pueden
# contener saltos de linea ni espacios porque al momento de la lectura nos 
# generara un error

# al momento de importar la base de datos generada con pprint necesitamos:

# deberia permitir ver los elementos contenidos en Data pero no esta dejando, puede ser dif en la version Data.Letras_griegas[0]
