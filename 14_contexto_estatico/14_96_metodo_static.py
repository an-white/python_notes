class Clase:
    var_clase="VARIABLE DO CLAISE :v"
    
    def __init__(self,var1) -> None:
        self.var1=var1

    # metodo estatico solo se asocia a la clase mas no a los objetos instanciado
    # este objeto no puede acceder a las variables de instancia
    @staticmethod
    def estatico():
        # el contexto estatico en python es todo lo que esta en la clase al ser cargada y el dinamico son los objetos que se pueden crear a partir de ella esto no permite acceder a las variables de instancia ni al self, solo se puede acceder a las variables de clase de manera indirecta de la siguiente manera
        print(Clase.var_clase)

    #metodo de clase
    @classmethod
    # def un parametro cls que es parametro de la clase en si misma
    def metodo_clase(cls):
        print(cls.var_clase)
        

# llamado de metodo estatico
Clase.estatico()

# llamado a metodo de clase
Clase.metodo_clase()

## el contexto dinamico puede acceder al contexto estatico ya que primero se carga la clase y luego se crean los objs en memoria