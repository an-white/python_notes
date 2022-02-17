class Cajas:
    # contador de objetos creados
    contador_cajas = 0

    @classmethod
    def counter_incrementer(cls):
        cls.contador_cajas += 1
        return cls.contador_cajas

    def __init__(self, volumen=10, peso=1) -> None:
        self.id_caja = Cajas.counter_incrementer()
        self.volumen = volumen
        self.peso = peso

    def __str__(self):
        return f"Caja n{self.id_caja} [Peso:{self.peso} | Volumen:{self.volumen}]"


Caja1 = Cajas(12, 4)

print(Caja1)
