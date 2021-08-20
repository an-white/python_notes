class FiguraGeometrica:
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