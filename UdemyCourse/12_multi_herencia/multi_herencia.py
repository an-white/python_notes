from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self,ancho,alto) -> None:
        self._ancho = ancho
        self._alto = alto

    # get and set property
    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self,ancho):
        self._ancho=ancho
    
    # get and set property
    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self,alto):
        self._alto=alto

    # al ser un metodo abstracto convierte a la clase en una clase abstracta, lo que se traduce en que la clase hija se oblige a implementar el metodo
    @abstractmethod
    def area(self):
        pass