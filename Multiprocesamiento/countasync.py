import asyncio
import random


async def count(a):
    t = random.randint(2, 10)
    print(f"tarea {a}")
    init = time.time()
    await asyncio.sleep(t)
    end = time.time()
    print(f"{end - init} tarea: {a} ")


async def main():
    await asyncio.gather(count(1), count(2), count(3))


if __name__ == "__main__":
    import time

    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter()
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
