# simulado de semaforos con Assertion

industras_15={'ns':'verde','ew':'rojo'}
comercio_12={'ns':'rojo','ew':'verde'}

def cambio_de_luces(semaforos):
    for key in semaforos.keys():
        if semaforos[key]=='verde':
            semaforos[key]='amarillo'
        elif semaforos[key]=='amarillo':
            semaforos[key]='rojo'
        elif semaforos[key]=='rojo':
            semaforos[key]='verde'
    assert 'rojo' in semaforos.values(), 'Ninguna luz esta en rojo '+ str(semaforos)

cambio_de_luces(industras_15)
print(industras_15)