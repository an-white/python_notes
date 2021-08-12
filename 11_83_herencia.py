# clase padre
from typing import Text


class Carro:
    def __init__(self,marca,puestos,año):
        self._marca = marca 
        self.puestos = puestos 
        self.año = año
    
    @property 
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self,marca):
        self._marca = marca

    def show_details(self):
        details = (f"Marca: {self._marca}, Puestos: {self.puestos}, Año: {self.año}")
        return details

    def call_test(self,kwargs):
        print(self.test(kwargs))

    def test(self,kwargs):
        text = f"integracion de {kwargs}"
        return text

    

# Clase hija
class CarroElectrico(Carro):
    def __init__(self, marca, puestos, año, autonomia):
        # heredando de la clase carro y pasandole los atributos de inicializacion
        super().__init__(marca, puestos, año)
        # def nuevos atributos dentro de la clase hija
        self.autonomia = autonomia

    def show_details(self):
        print(f"{super().show_details()} Autonomia: {self.autonomia}")
            
    

carro = Carro("BMW",4,2021)
print(carro.marca)

carro.marca = "Porsche"
print(carro.marca)
print(carro.show_details())

# objeto hijo instanciado
carro_electrico = CarroElectrico("Tesla",4,2021,"500km")
print(carro_electrico.marca)
carro_electrico.show_details()
carro.call_test({"key":"value"})