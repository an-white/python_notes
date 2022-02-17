# Metodo .findall()
# esto regresara una list con todos los elementos conseguidos 
# en el texto analizado 
import re

txt = '''Hola como estas?
Muy bien y tu que haces?
nada estoy descansando 
bien por ti'''

Regex = re.compile(r'Hola|que haces|bien por')
txt1 = Regex.findall(txt)
print(txt1)

# Abreviaciones de codigo para busquedas generales

Regex = re.compile(r'\d')  # reperesenta cualquier valor numerico [0,9]

Regex = re.compile(r'\D')  # representa cualquier valor que no sea numerico

Regex = re.compile(r'\w')  # representa cualquier valor alfanumerico o guion bajo la

Regex = re.compile(r'\s')  # representa cualquier espacio, tab, o salto de linea

Regex = re.compile(r'\S')  # representa cualquier cualquier caracter que no sea un espacio, tab o salto de linea

# Apliacion de las abreviaciones
Regalos = ['12 perritos', '3 RC', '2 Helicopteros', '4 carritos', '10 muñecas']
Cadena = ', '.join(Regalos)
print(Cadena)

Regex0 = re.compile(r'\d+\s\w+')
Lista_Regalos = Regex0.findall(Cadena)
print(Lista_Regalos)

# Buscar elementos especificos con Regex
# esto se determina con diferentes clases definidas entre []

# para conseguir vocales mayusculas y minusculas
Regex = re.compile(r'[aeiouAEIOU]')
Lista_Regalos = Regex.findall(Cadena)
print(Lista_Regalos)

# para conseguir valores alfanumericos la ñ no forma parte de esta clase
Regex1 = re.compile(r'[a-zA-z0-9]')
Lista_Regalos = Regex1.findall(Cadena)
print('\n')
print(Lista_Regalos)

# si se desea definir los valores que NO se desean buscar en el str 
# se def [^clase omitida] 

Regex2 = re.compile(r'[^a-zA-Z0-9]')
Lista_Regalos = Regex2.findall(Cadena)
print('\n')
print(Lista_Regalos)

# si se desea conseguir un cierto inicio en la cadena analizada se 
# utiliza el '^seguido de la cadena buscada'

Regex3 = re.compile(r'^Hola')
Comienza = Regex3.search(txt)
print(Comienza)

# esta impresion dara como resultado la longitud de la cadena 
# encontrada si fue encontrado el objeto y cual objeto fue encotrado

# otra forma de conseguir objetos pero que terminen en con 
# ciertos parametros se utiliza el $ al final de la definicion que 
# se desea encontrar 

txt1 = 'Your number is 42'
Regex = re.compile(r'\d+$')
p = Regex.search(txt1)
print(p)

# con el . se pueden definir tambien busquedas de cadenas que posean
# cierta terminacion y posean previamente 1 solo caracter indefinido

Regex = re.compile(r'.a')
p = Regex.search(txt)
print(p)

# combinando (.*) se puede conseguir una cadena completa de un
# objeto de longitud n que este acompañado de ciertos caracteres
# y se ve interrumpida por los saltos de linea
txt = 'Nombre: An Apellido:Shao'
Regex = re.compile(r'Nombre: (.*) Apellido:(.*)')
p = Regex.search(txt)
print(p.group(1) + ' ' + p.group(2))

txt = '<para servir hay> que saber servir>'
Regex = re.compile(r'<.*>')
p = Regex.search(txt)
print(p.group())

# el greedy mode de Regex permite abarcar la mayor longitud de
# ciertas cadenas def de forma general esto se puede evitar
# colocando ? para que python desactive este modo y trabaje con 
# la primera cadena encontrada

Regex = re.compile(r'<.*?>')
p = Regex.search(txt)
print(p.group())

# Matching saltos de lineas con .* y el .DOTALL()
# el (.*) permite conseguir cualquier elemento execto los saltos de linea
# pero si se introduce el modulo .DOTALL se puede mostrar todos los 
# elementos escritos textualemente en una cadena

txt = '''Hola como estas?
Muy bien y tu que haces?
nada estoy descansando 
bien por ti'''
Regex = re.compile('.*', re.DOTALL)
analizer = Regex.search(txt)
print(analizer.group())

# con el .DOTALL podemos visualizar todos los elementos introducidos
# en el str esto permite de forma comoda tomar todo el texto introducido
# incluyendo saltos de lineas de forma comoda
