# una funcion recursiva consiste en
# el llamado de una funcion a si misma n veces hasta que se cumpla alguna condicion deseada

def fact(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * fact(num-1)

num = int(input("introducir numero entero "))
result = fact(num)
print("factorial de ", num, " es: ", result)

# se pueden añadir atributos a objetos de clases instanciadas en python