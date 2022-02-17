def check(item, l, r):  # l y r son las dimensiones que se desean colocar a la factura
    s = 0
    print('Compra de'.center(l + r, '='))
    for i, a in checklist.items():
        print(i.ljust(l, '.') + str(a).rjust(r))
    for k, v in checklist.items():
        s = checklist.values()
    print('Cantidad total productos'.ljust(l, '>') + str(s).rjust(r))


checklist = {'Sandwhic': 4, 'Mangos': 10, 'Fresas': 29, 'Vasos': 4, 'Piñas': 2, 'Galletas': 20}
check(checklist, 10, 10)
