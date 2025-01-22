import asyncio
import time
from math import factorial


async def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


async def square(n):
    return n * n


async def cube(n):
    return n ** 3


async def calculate_all(numbers):
    fibs = await asyncio.gather(*(fibonacci(n) for n in numbers))
    facts = await asyncio.gather(*(asyncio.to_thread(factorial, n) for n in numbers))
    squares = await asyncio.gather(*(square(n) for n in numbers))
    cubes = await asyncio.gather(*(cube(n) for n in numbers))
    return fibs, facts, squares, cubes


async def main_async():
    numbers = list(range(1, 11))
    start_time = time.time()
    results = await calculate_all(numbers)
    print("Asynchronous Execution Time:", time.time() - start_time)
    return results



async_results = asyncio.run(main_async())
