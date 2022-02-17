class Clase:
    """
    las variables de clase son variables las cuales pertenecen a la clase y
    la cuales pueden ser accedidas por todos los objetos de dicha clase y
    modificarla para poder crear una variable de clase se def fuera del metodo init
    """
    var_clase = "VARIABLE DO CLAISE :v"

    def __init__(self, var1) -> None:
        self.var1 = var1


# para acceder a una variable de clase no es necesario generar un objeto
print(Clase.var_clase)
caja_1 = Clase("immstancia")

print(caja_1.var1)
print(caja_1.var_clase)
"""
esta variable de clase puede ser modificada pero solo se refleja en el objeto
para poder modificarla completamente la variable de clase debe ser modificada mediante la clase
y asi conserva la referencia en memoria y
todos los objetos actualizaran podran consultar el valor actualizado
"""
Clase.var_clase = 29
caja_1.var_clase = 12

print(Clase.var_clase)
print(caja_1.var_clase)

obj2 = Clase("cosa")
print(obj2.var_clase)
# modificacion de la variable de clase

print(Clase.var_clase)
print(caja_1.var_clase)

# creacion de variables de clase al vuelo o al momento de necesitarlo
Clase.casa = "caisa"
print(Clase.casa)
print(caja_1.casa)
