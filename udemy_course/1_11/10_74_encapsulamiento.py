class Carro:
    def __init__(self, marca, puestos, año):
        """
        a este atributo no se deberia poder acceder para poder acceder
        a el se utiliza un decorador property para acceder indirectamente a este atributo
        """
        self._marca = marca
        self.puestos = puestos
        self.año = año

    @property  # permite acceder al atributo fuera de la clase
    def marca(self):
        return self._marca

    """
    permite cambiar el valor del atributo fuera de la clase
    si no se define el decorador setter esto genera un atributo de solo lectura
    y dara un error si se intenta modificar
    """

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    def show_details(self):
        print(f"Marca: {self._marca}, Puestos: {self.puestos}, Año: {self.año}")

    # metodo destructor de objeto de manera explicita
    def __del__(self):
        print(f"Eliminando Carro Marca: {self._marca}, Puestos: {self.puestos}, Año: {self.año}")


carro = Carro("BMW", 4, 2021)
# acceder al atributo con el nombre del metodo def en la linea 9 gracias al decorador property
print(carro.marca)

# modificar con el setter el atributo permite tratar a la funcion como un atributo del objeto
carro.marca = "Porsche"
print(carro.marca)
carro.show_details()
