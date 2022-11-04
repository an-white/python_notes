import asyncio
import random
import time
from concurrent.futures import ThreadPoolExecutor as TPE


def super_task(a):
    init = time.time()
    t = random.randint(2, 10)
    time.sleep(t)
    end = time.time()
    print(f"{end - init} tarea: {a} ")


async def call_tasks():
    executor = TPE(max_workers=1)
    for n in range(4):
        executor.submit(super_task, n + 1)
        executor.submit(super_task, (n + 1) * 2)
    return "vista de retorno"


async def main():
    return await asyncio.gather(call_tasks())


if __name__ == "__main__":
    print(asyncio.run(main())[0])
