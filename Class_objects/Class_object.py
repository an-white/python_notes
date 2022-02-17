# objeto entidad con caracteristicas que realiza det acciones
# clase permite generar n cantidad de objetos 

class Lapiz:  # se debe comenzar con mayuscula y no se puede utililzar _
    # a continuacion se colocan todos los atributos y acciones que puede realizar esta clase
    color = 'amarillo'
    contiene_borrador = False
    usa_grafito = True

    # una clase puede contener una funcion "Metodo" para poder hacer esto se debe colocar entre (self)
    # Metodo de class
    def dibujar(self):
        print('lapiz dibujando ...')

    # Metodos condicionados a Atributos de la clase
    def borrar_si(self):
        self.contiene_borrador = True  # esto regresara si exite o no la condicion requerida

    # metodo que depende de otro metodo
    def borrar(self):
        if self.contiene_borrador == True:  # si se def de esta forma el tomara el valor del metodo en true or false para envaluar en el condicional
            print('El lapiz borra...')
        else:
            print('No se puede borrar')


# en python todo es un objeto

l_gen = Lapiz()

# el objeto son todas las librerias importadas y todo esto un objeto que contiene det caracteristicas por def
# estas caracteristicas se den como atributos y Metodos son las funciones
l_gen.color
l_gen.dibujar()
l_gen.borrar()


# lo que este contenido dentro de () en un Metodo son los valores que el tomara para luego retornar las mod
# que el este programado a realizar


# para heredar caracteristicas de una clase se define de la siguiente manera
# con esta declaracion se heredan todas las caracteristicas de la clase principal a la hija
class Portaminas(Lapiz):
    pass


p = Portaminas()
p.borrar_si()
p.borrar()
