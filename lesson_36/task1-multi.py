from multiprocessing import Pool, cpu_count
import time
from math import factorial


def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def square(n):
    return n * n


def cube(n):
    return n ** 3


def calculate_all_multiprocessing(numbers):
    with Pool(cpu_count()) as pool:
        fibs = pool.map(fibonacci, numbers)
        facts = pool.map(factorial, numbers)
        squares = pool.map(square, numbers)
        cubes = pool.map(cube, numbers)
    return fibs, facts, squares, cubes


def main_multiprocessing():
    numbers = list(range(1, 11))
    start_time = time.time()
    results = calculate_all_multiprocessing(numbers)
    print("Multiprocessing Execution Time:", time.time() - start_time)
    return results


if __name__ == "__main__":
    numbers = list(range(1, 11))
    start_time = time.time()
    results = calculate_all_multiprocessing(numbers)
    print("Multiprocessing Execution Time:", time.time() - start_time)
    print("Results:", results)
