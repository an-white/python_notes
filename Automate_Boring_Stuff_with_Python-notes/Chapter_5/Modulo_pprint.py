# Modulo pprint
# se puede utilizar para mostrar las key y sus valores en forma de par
# ordenado, y mostrando cada key en una linea diferente

import pprint

sms = 'Que bueno que ya lo instalaste en todas partes'
count = {}
for c in sms:
    count.setdefault(c, 0)
    count[c] = count[c] + 1
pprint.pprint(count)

# Esta estructura permite contar cada caracter y a su vez mostrarlo
# de forma separada en pares ordenados de keys y valores de keys
print('\n')

print(pprint.pformat(count))
# Esta ultima estructura algo mas larga permite hacer la misma impresion
# que el pprint.pprint
