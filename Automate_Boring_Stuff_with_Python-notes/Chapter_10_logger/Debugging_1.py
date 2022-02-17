"""
mientras el try and except establecidos permiten al programa contiunar
de un error el cual se puede anticipar que va a suceder
con el key word raise se pueden def tambien estas exceciones que se
preveen para que el programa no falle

keyword raise acompañada de la excecion permite
raise Exception('Este es el mensaje de error')
"""


def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Debe colocarse 1 solo simbolo')
    if width <= 2:
        raise Exception('width debe ser mas grande que 2')
    if height <= 2:
        raise Exception('heigth debe ser mayor a 2')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as err:
        print('Ha ocurrido un error: ' + str(err))
