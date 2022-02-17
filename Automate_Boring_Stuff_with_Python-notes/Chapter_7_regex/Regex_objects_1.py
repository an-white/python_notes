# re permite analizar cadenas de texto de forma mas corta
import re
import sys

Check_Regex = re.compile(r'\d{3}-\d{3}-\d{4}')
# Esta vaiable contiene al objeto Regex que queremos buscar
# el escribir r'y el resto de slash invertidos es la mejor forma 
# de hacerlo

# Metodo seach del objeto Regex
# Da como mensaje None si no es encontrado el patron en el string
# si es encontrado devolvera el valor Match 
# el match tiene dentro de Regex un metodo group() el cual permite
# mostrar el objeto encontrado en el str que cumpla con las 
# condiciones establecidas
while True:
    print('\nIntroduzca un texto para verificar si este contiene un numero de TLF con al estructura ###-###-####')
    TLF = Check_Regex.search(input())
    if TLF == None:
        print('No se han econtrado numeros en el texto introducido')
    else:
        print('Numero de Tlf encontrado:' + TLF.group())
        sys.exit()

# Metodos del Regex
# re.DOTALL ignora saltos de lineas
# re.I identifica directamente la cadena buscada no distigue mayusculas
# o de minusculas
# re.VERBOSE permite utilizar saltos de linea en el Regex y al ejecutar
# el programa unira en una sola linea todo los parametros establecidos 
# en el REGEX
