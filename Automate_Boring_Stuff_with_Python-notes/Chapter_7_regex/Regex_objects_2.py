# Agrupando valores encontrados con objeto Regex
# la cadena a buscar puede ser separada en partes mediante () y
# estas se pueden mostrar a travez de group() siendo 
# group(0) o con el plural groups() todo el texto, group(1) la 1ra
# parte de la cadena buscada, group(2) la 2da etc...
import re

Check = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
Tlf = Check.search(input())
if Tlf != None:
    print(Tlf.group(0) + '\n')
    print(Tlf.groups())  # con Groups los imprime como tuplas los pedazos conseguidos por Regex
    print('\n' + Tlf.group(1) + '\n')
    print(Tlf.group(2) + '\n')
    print(Tlf.group(3) + '\n')
    Codigo_area, primeros_3D, ultimos_4D = Tlf.groups()
else:
    print('No existen numero con la estructura establecida')
# con groups se puede asignar valores del group como si de una tupla 
# se tratara a una  antidad de n variables 

# | Perimite hacer una busqueda separada en la misma definicion del Regex
# Este caracter es interprentado como un or y si las cadenas buscadas
# existen mas de 1 vez este traera como resultado la primera que encuentre
txt = '''Hola como estas?
Muy bien y tu que haces?
nada estoy descansando 
bien por ti'''
# el Regex se detendrá al conseguir el primer elemento que sea identico
# a los valores establecidos

Regex = re.compile(r'Hola|que haces|bien por')
txt1 = Regex.search(txt)
txt2 = Regex.search(txt)
print(txt1.group())

# Se puede establecer subgrupos de busqueda dentro de Regex para 
# disminuir la longitud de la linea de cogido, esta linea establece
# el orden de busqueda en las str leidas

Regex1 = re.compile(r'H(ola|ello|i|olis)')
diag = 'Hola amigo que tal tu dia'
diag2 = 'Hello todo bien'
txtd1 = Regex1.search(diag)
txtd2 = Regex1.search(diag2)
print(txtd1.group() + ' ' + txtd2.group())

# Si se desea buscar un str el cual posee una parte opcional se puede
# recurrir al simbolo de ? el cual permite introducir entre() la parte
# opcional de la cadena

# Para poder buscar un | se debe usar \| para que sea reconocible como texto

txt = 'amortiguador'
txt1 = 'amor'
Regex2 = re.compile(r'am(ortiguad)?or')  # el ? debe preceder el () de la parte opcional
s1 = Regex2.search(txt)
s2 = Regex2.search(txt1)
print(s1.group() + ' ' + s2.group())

# Encontrar 0 o mas con *
# esto permite conseguir textos que contengan o no un pedazo que se 
# desea conseguir este pueder estar desde 0 hasta n veces en el str analizado

txt = 'banananananananan'
txt1 = 'banana'
txt2 = 'bana'
Regex3 = re.compile(r'ba(na)*na')
s1 = Regex3.search(txt)
s2 = Regex3.search(txt1)
s3 = Regex3.search(txt2)
print(s1.group() + ' ' + s2.group() + ' ' + s3.group())

# Match 1 o mas veces con +
# funciona de igual manera que el Match con * pero a diferencia del *
# este solo encuentra valor que aparezcan 1 o mas veces
txt = 'banananana'
Regex4 = re.compile(r'ba(na)+na')
s1 = Regex4.search(txt)
print(s1.group())

# Conseguir patrones repetitivos en un cierto periodo de veces
# en el Regex se establece (lo que se busca){la cantidad de repeticiones buscadas}

Regex5 = re.compile(r'(je){3,4}')

# en este se puede establecer {cantindad min de repeticiones, cantidad max de repeticiones
