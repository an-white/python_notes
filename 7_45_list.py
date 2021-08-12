# para eliminar un elemento por su indice se puede utilizar la funcion pop
l=list(range(4))
print(l)
# por defecto se elimina el ultimo valor
l.pop()
print(l)
# para eliminar el elemento i de la list se coloca el indice a eliminar
l.pop(0)
print(l)
# eliminar todo dentro de la list
l.clear()
print(l)

# para definir una tupla de 1 elemento se debe colocar al final del mismo una , para que sea identifacado como tupla