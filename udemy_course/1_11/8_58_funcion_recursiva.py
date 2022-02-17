# una funcion recursiva consiste en
# el llamado de una funcion a si misma n veces hasta que se cumpla alguna condicion deseada

def fact(val):
    if val == 1 or val == 0:
        return 1
    else:
        return val * fact(val - 1)


num = int(input("introducir numero entero "))
result = fact(num)
print("factorial de ", num, " es: ", result)

# se pueden añadir atributos a objetos de clases instanciadas en python
