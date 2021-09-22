# sobrecarga de un operador significa que un operador se puede comportar de diferentes formas por ejemplo el simbolo + que contanena y suma
class Box:
    def __init__(self,weight):
        self.weight = weight

    # se sobreescribe un operador sobrecargado y se añade la operacion deseada la logica es traer al mismo objeto y al otro que se desea utilzar para operar
    def __add__(self,other):
        return self.weight + other.weight

    def __sub__(self,other):
        return self.weight - other.weight
    
box_1=Box(22)
box_2=Box(12)

print(f"Total weight: {box_1 + box_2}")
print(f"weight diferential : {box_1 - box_2}")