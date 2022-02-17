# Modulos de remocion de espacios vacios en str al inicio y al final 
# del str
b = '             Hola amigo como estas?     '
print(
    'Eliminado a ' + b.strip() + ' ambos lados\n solo a ' + b.lstrip() + 'izquierda\nsolo a' + b.rstrip() + ' derecha')

"""
Copiar y pegar str con el Modulo pyperclip 

Permite pegar cosas que se encuentren en el portapapeles del PC
y copiar elementos que se pueden utilizar fuera de python
"""

import pyperclip

print('Con este modulo puedes ver lo que está copiado en el portapapeles del PC' + str(pyperclip.paste()))
pyperclip.copy('He salido de las entrañas de Python y tu?')

# Hacer el proyecto en la pagina 160
