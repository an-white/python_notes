from color import Color
from multi_herencia import FiguraGeometrica


class Square(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # accediendo a los atributos y metodos de la clase padre si se quiere llamar mas de 1 se debe estructurar de la siguiente forma
        # con esto se inicializan los valores de las clases padre
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def area(self):
        return self.ancho * self.alto


if __name__ == "__main__":
    # inicializar objeto
    cuadrado = Square(3, "azul")

    # acceso a sus atributos
    print(cuadrado.area())

    # permite visualizar el orden en el que se ejecutaran los metodos en la jerarquia de clases que se ha definido
    print(Square.mro())
