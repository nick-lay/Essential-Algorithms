import math
from typing import List


def find_primes(max_number: int) -> List[int]:
    """
    Поиск простых чисел от 1 до max_number. Решето Эратосфена.
    Search of Prime numbers from 1 to max_number. The Sieve Of Eratosthenes.
    """
    is_compose = [False] * max_number
    for i in range(4, max_number, 2):
        is_compose[i] = True
    next_prime = 3
    stop_at = math.sqrt(max_number)
    while next_prime < stop_at:
        for i in range(next_prime*2, max_number, next_prime):
            is_compose[i] = True
        next_prime += 2
        while next_prime <= max_number and is_compose[next_prime]:
            next_prime += 2
    return [number for number, value in enumerate(is_compose[1:], 1) if not value]
