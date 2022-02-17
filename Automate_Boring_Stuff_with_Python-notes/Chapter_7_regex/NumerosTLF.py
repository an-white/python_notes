"""
Verificacion de patrones en str
Estas verificaciones son realizadas preferiblemente con un modulo definido
antes de la ejecucion del codigo
"""


# este programa verificara la estructura que debe tener un numero tlf

# Modulo de verificacion de numeros
def NumeroTLF(txt):
    global Nro
    if len(Nro) != 12:
        return False
    for i in range(0, 3):
        if not Nro[i].isdecimal():
            return False
    if Nro[3] != '-':
        return False
    for i in range(4, 7):
        if not Nro[i].isdecimal():
            return False
    if Nro[7] != '-':
        return False
    for i in range(8, 12):
        if not Nro[i].isdecimal():
            return False
    return True


# Modulo de busqueda
def Find(txt):
    global TLFs
    for c in range(len(Nro)):
        search = Nro[
                 c:c + 12]  # esto define que el buscador armara cadenas desde i hasta i+12 y si estas cumplen con la estructuras seran validas
        if NumeroTLF(search):
            print('Se ha encontrado el(los) numero(s) telefonico(s):' +)


while True:
    print('\nIntroduzca su numero telefonico, este debe poseer la estructura, ###-###-####')
    Nro = input()
    Find(Nro)
    if NumeroTLF(Nro) == True:
        print('El numero ' + str(Nro) + ', es valido.')
        break
    else:
        print('El numero introducido no posee la estructura de Numero telefonico')
