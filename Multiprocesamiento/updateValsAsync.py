import asyncio
import random
import time


async def super_task(x):
    init = time.time()
    t = random.randint(1, 5)
    time.sleep(t)
    end = time.time()
    x.append(end - init)


async def main():
    val_list = []
    for i in range(5):
        await super_task(val_list)
        print(val_list)


if __name__ == '__main__':
    asyncio.run(main())
