#Cap 6 el cual está enfocado en la manipulacion de strings y como
# se puede jugar con esto para realizar ciertos ajustes


# si se desea colocar un apostrofe en un string se debe encerrar
# entre Dobles comillas para que el apostrofe el compilador lo
# lea como tal
txt="vamos pa' donde Luis"
print(txt)

# El slash invertido permite colocar caracteres que python
# entiende como parte del codigo y perimite realizar
# acciones que normalmente no estan permitidos

print('\' , \" , \t , \n , \\')

#Raws strings, se generan al colocar r antes de las comillas
# y este tipo de str lee textualmente todo lo que se encuentre
# contenido dentro de las comillas y en este tipo de str no
# se pueden leer las comillas directamente se debe cambiar
# el tipo de comillas para que estas aparezcan

print(r"Como esta' la vaina ")

# las triples comillas simples logran interpretar los saltos
# de linea dentro del codigo sin tener que colocar \n

print(''' 
Como estas me llamo triple comilla
logro separar todo cada vez que desees
por eso normalmente soy muy util
''')

# operador in y not in permite buscar fracciones o cadenas de texto
# dentro de otra cadena de texto existente
t1='''operador in y not in permite buscar fracciones o cadenas de texto
dentro de otra cadena de texto existente'''
print(t1)
#print('''
# Introduce la palabra que deseas buscar dentro del texto''')
# p=input()
print('Está la palabra texto'+ 'texto' in t1)

# Metodo .upper()
# coloca en mayuscula todos los caracteres dentro del str

txt1='hi my friend'
print(txt1.upper()+'''
''')

# Metodo .lower 
# coloca todo el texto de un str en minuscula
print(txt.lower())

# La utilidad de estos metodos recae en dialogos interactivos en 
# donde el usuario puede introducir mayusculas intercaladas en el
# texto creando desigualdades de texto entre lo introducido y lo esperado
# por el programa, estos metodos no modifican la cadena inicial pero si, 
# generan una temporal mientras es utilizada

print('Como te sientes hoy?')
s=input()
if s.lower()== 'bien':
    print('Me alegra mucho C:')
else:
    print('Espero que el resto de tu dia sea mejor :l')

# Metodos .islower , .isupper
# dan como resultado booleanos y permiten verificar si el str
# seleccionado esta en mayuscula o en minuscula 

print(str(s.isupper())+ ' '+ str(s.islower()))

# otros metodos .isX para validar inputs de usuarios
print('''
introduzca el texto a evaluar''')
texto=input()
print('verifacacion de solo letras '+str(texto.isalpha()))
print('verificacion alfanumerica '+str(texto.isalnum()))
print('verificacion numerica '+str(texto.isdecimal()))
print('verifica que solo sean espacios, tab, pero no vacios '+str(texto.isspace()))
print('verifica que todas las palabras comiencen en mayusculas y puede contener numeros '+str(texto.istitle()))

#Con esto se puede comenzar el programa de resortes.py

# Metodos .startwith(), endwith()
# su funcion es verificar el inicio y el fin respectivamente de str()
# estos pueden verificar desde 1 caracter hasta una palabra o frase
print(str(s.startswith('bi')))
print(str(s.endswith('en')))

#.join()
# permite transformar una lista de str en un str y definir el separador
# del str que se desea mostrar

f=' '.join(['perros','Gatos', 'Garabatos'])
g='-ABCMUNDO-'.join(['perros','Gatos', 'Garabatos'])
print(f)
print(g)

#.split 
# transforma un str en una list transformando por defecto los 
# espacios vacios en los separadores de la lista, pero estos separadores
# pueden ser definidos por el usuario
print(g.split('-ABCMUNDO-'))
print(f.split())

# alineacion de texto
# metodos permiten añadir espacios o caracteres de separacion a un
# texto def de la siguiente forma

#.Tipo de alineacion(cantidad de espacios,Relleno de espacio a colocar debe ser un solo elemento)

p0='Hola'.ljust(30,'=')
p1='Usuario'.rjust(30,'=')
p='Bienvenido'.center(30,'▄')
p3='A mi nueva interfaz'.center(30,'▀')
print(p0+'\n'+p1+'\n'+p+'\n'+p3+'\n')