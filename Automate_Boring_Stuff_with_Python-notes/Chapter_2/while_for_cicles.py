#while ciclo que se repite mientras se cumpla o no una condicion
#hacer un while para una variable no declarada previamente
#se establece la condicion de true or false la cual
#establece que mientras eso se cumpla se repita el loop

while True:
    print('escribe tu nombre')
    name= input()
    if name != '':
        break #Si el nombre es diferente de vacio se acaba el ciclo
print ('Bienvenido ' + name)

# Estructura de ciclo for, con un contador i y un det range(n)
#n def el numero de veces que se repetira dicho ciclo

for i in range(2):
    print('Mi nombre es IA-032120 ' + str(i) )

#el range puede ser definido de la siguiente manera

for f in range(20,-20,-2):
#donde el primer numero es el primer valor en el range
#2do numero es el fin del range
# el tercer numero es el salto de cada valor en el range
# el salto puede ser negativo lo que signifacara que el range ira disminuyendo de valor con el salto indicado
# el 0 se tomara en cuenta en la cantidad de valores tomados en el rango
# es decir si el range pasa por 0 y se necesita llegar a un valor x se tendra que terminar el
# range en x+salto si el range va de mayor 
    print(f)
