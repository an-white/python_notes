# IMPORTANTE: para conseguir cierta estructura compleja definida 
# tiene que estar encerrada su def entre ()

# ? permite conseguir 0 o 1 vez lo que lo antecede
# * permite conseguir 0 o mas veces lo que lo antecede
# + permite conseguir 1 o mas veces lo que lo antecede
# {n} encuetra exactamente n el elemento que lo antecede
# {n,} encuetra n o mas veces el elemento que lo antecede
# {,m} encuentra de 0 a m veces el elemento que lo antecede
# {n,m} encuentra al menos n y un max de m veces el elemento que lo antecede
# {n,m}? *? +? encuentra la cadena mas corta del elemento que lo antecede
# ^cadena permite conseguir str que comiencen con el elemnto cadena 
# $cadena permite conseguir str que terminen con el elemento cadena
# . permite conseguir cualquier caracter alfanumerico y espacios execto los saltos de linea
#  \d, \w, \s encuentra cualquier digito, letra, o espacio respectivamente
# \D, \W, \S encuentra cualquier valor execto digitos, letras o espacios respectivamente
# [abc] encuentra cualquier valor entre los []
# [^abc] encuentra cualquier valor execto los que se encuentran entre []

# Match indiferente de mayusculas y minusculas con
# re.I o re.IGNORECASE dentro de re.compile()

import re

txt = 'RoboCop is part man, part machine, all cop.'
Regex = re.compile(r'robocop', re.I)
Diag = Regex.search(txt)
print(Diag.group())

# sustitucion de caracteres en un str con el Metodo .sub
# permite sustituir valores de una cadena de entrada con algo que 
# se desee sustituir 
txt = 'Agent Alice gave the secret documents to Agent Bob'
Regex_C = re.compile(r'Agent \w+')
NC = Regex_C.sub('CENSURADO', txt)
print(NC)

# para reemplazar se debe definir
# regex=re.compile(r'Lo que se desea reeemplazar y un elemento que lo def')
# despues al ejecutar la busqueda
# regex.sub('Valor sustituto',str donde se sustituira este dicho valor)
# para hacer print se debe asociar el ultimo elemento a una variable
# la cual se asignara como un str


# Tambien se puede sustituir parcialmente una cadena si se define 
txt = '''Agent Alice told Agent Carol that Agent Eve
knew Agent Bob was a double agent'''
Regex_PC = re.compile(
    r'Agent (\w)\w*')  # esta definicion establece la palabra clave, lo que se desea conservar y lo que se piensa sustituir
NC = Regex_PC.sub(r'\1***',
                  txt)  # en r'\[n valores que se desean mostrar]acompañado de lo que se desea colocar como relleno'
print(NC)

# estructura compleja para identificar numeros telefonicos, 
# con o sin codigos de area 

# para establecer una busqueda mas organizada con mas variables se
# utiliza el .VERBOSE() dentro del .compile en conjunto con '''
# lo cual permite escribir en varias lineas las definiciones de 
# lo que se desea buscar haciendo mas facil su posterior lectura

IDTLF = re.compile(r'''(
(\d{3}|\(\d{3}\))?                  # Codigo de area Opcional puede estar entre ()
(\s|-|\.)?                          # Tipo de separador
\d{3}                               # primeros 3 digitos
(\s|-|\.)                           # Tipo de separador
\d{4}                               # Ulitimos 4 digitos
)''', re.VERBOSE)

txt = 'contactos al 412.405.6128 y 416 648 1139 o 241.858 6237'
Matched = IDTLF.findall(txt)
print(Matched)
