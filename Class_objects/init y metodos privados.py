# Metodo init
# permite establecer parametros iniciales a una clase
class Cohete:
    # Valores iniciales 
    def __init__(self,p,o,l):# despues del self se def que parametros se desean introducir en el metodo
        self.pais=p
        self.contiene_O_l=o
        self.__plt_lanzamiento=l# si el atributo comienza con __ es un atributo privado
        # esto significa que solo puede ser modificado por la clase y no por las instancias
    # si se desea que cada variable tenga valores por defecto se coloca variable=Valor por def

# esta es la forma de poder acceder al metodo privado desde la clase
    def get_plt_lanzamiento(self):
        return self.__plt_lanzamiento

    def launch(self,pais='US',contiene_O_l='s',plt_lanzamiento='Cabo Cañaberal'):
        print('Calculando trayectoria...')
        print('''Resumen de datos: 
            Pais: '''+pais+'''
            Contiene Oxigeno Liquido: '''+contiene_O_l+'''
            Plataforma de lanzamiento: '''+ plt_lanzamiento)

print('Pais del Cohete')
p=input()

print('Cohete con Oxigeno liquido?')
o=input()
if o.lower()=='s':
    o = True
else:
    o = False
    
print('Lugar de lanzamiento')
l=input()
Lanzamiento=Cohete(p,o,l) #Asignando que variables se asignan al metodo

Lanzamiento.launch()