import logging
import random
import time
from concurrent.futures import ThreadPoolExecutor as TPE

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def super_task(a):
    init = time.time()
    t = random.randint(2, 10)
    time.sleep(t)
    end = time.time()
    logging.info(f'terminamos tarea nro:{a}, de duracion {end - init} init: {init} end: {end}\n ')


if __name__ == '__main__':
    executor = TPE(max_workers=6)

    # para usar threads las tareas se deben declarar en el mismo nivel y ejecutar una debajo de la otra para que estas se tomen todas de una vez despues el resutado se arrojara 1 a 1 conferme vayan terminando su ejecucion
    n = 0
    while True:
        executor.submit(super_task, n)
        executor.submit(super_task, n + 1)
        executor.submit(super_task, n + 2)

        n += 3
        if n >= 30:
            break
