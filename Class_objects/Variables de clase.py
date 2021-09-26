class Circulo:
    pi=3.14 # para def variables inmutables de coloca _ antes de def el nombre 
    def __init__(self, radio):
        self.radio=radio 

    def area(self):
        return (self.radio**2)*self.pi
        
print(Circulo.pi)

c_1=Circulo(4)
c_2=Circulo(3)

print(c_1.radio) # Si no se def el metodo a mostrar python dara como msg el objeto que fue asignado a dicha variable
print(c_2.radio)

print(c_1.__dict__) # esto nos mostrara los atributos contenidos en el objeto 

print(c_1.area())
