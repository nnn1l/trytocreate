import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


NUMBERS = [
    2,  # prime
    1099726899285419,
    1570341764013157,  # prime
    1637027521802551,  # prime
    1880450821379411,  # prime
    1893530391196711,  # prime
    2447109360961063,  # prime
    3,  # prime
    2772290760589219,  # prime
    3033700317376073,  # prime
    4350190374376723,
    4350190491008389,  # prime
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,  # prime
]


def filter_primes(executor_class):
    with executor_class() as executor:
        results = list(executor.map(is_prime, NUMBERS))
    return [num for num, is_prime_flag in zip(NUMBERS, results) if is_prime_flag]

def test_thread_pool():
    start_time = time.time()
    primes = filter_primes(ThreadPoolExecutor)
    duration = time.time() - start_time
    return primes, duration


def test_process_pool():
    start_time = time.time()
    primes = filter_primes(ProcessPoolExecutor)
    duration = time.time() - start_time
    return primes, duration


if __name__ == "__main__":
    thread_primes, thread_time = test_thread_pool()
    process_primes, process_time = test_process_pool()

    print("ThreadPoolExecutor Results:")
    print(f"Primes: {thread_primes}")
    print(f"Time: {thread_time:.4f} seconds\n")

    print("ProcessPoolExecutor Results:")
    print(f"Primes: {process_primes}")
    print(f"Time: {process_time:.4f} seconds")
