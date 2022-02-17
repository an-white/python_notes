import asyncio


async def mygen(u: int = 10):
    """Yield powers of 2."""
    i = 0
    while i < u:
        yield 2 ** i
        i += 1
        await asyncio.sleep(0.1)


async def main():
    g = [i async for i in mygen(5)]
    f = [j async for j in mygen(2) if not (j // 3 % 5)]
    return f, g


if __name__ == '__main__':
    f, g = asyncio.run(main())
