# tipo de coleccion set
# permite almacenar objetos:
# de forma desordenada
# que no esten duplicados
# no es posible modificar dichos objetos
# permite añadir y eliminar objetos

container = {"boxes","tires", "motor", "turbo"}
print(container,len(container))

# verificar elemento
print("motor" in container)

# add elemento
container.add("volant")
print(container,len(container))

# eliminar elemento existente
container.remove("volant")
print(container,len(container))

# descartar un elemento exista o no
container.discard("volants")
print(container)

# vaciar un set 
container.clear()

