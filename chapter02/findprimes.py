import math
import random
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


def _raise_to_power_by_module(x: float, y: int, module: int) -> float:
    """
    Остаток числа x в степени y.
    """
    power = 1
    value_power = x
    power_values = {1: x}
    while power+1 <= y:
        power *= 2
        value_power = value_power*value_power % module
        power_values[power] = value_power
    result = 1
    for power in sorted(power_values, reverse=True):
        if power <= y:
            result = power_values[power]*result % module
            y -= power
            if y == 0:
                break
    return result


def is_prime(number: int, max_tests: int = 100) -> bool:
    """
    Является ли число простым.(Малая теорема Ферма).
    """
    for _ in range(max_tests):
        n = random.randint(1, number-1)
        if _raise_to_power_by_module(n, number-1, number) != 1:
            return False
    return True


def find_prime(num_digits: int = 10, max_tests: int = 100) -> int:
    """
    Найти случайное простое(возможно) число.
    """
    while True:
        number = random.randint(10**(num_digits-1), 10**num_digits)
        if is_prime(number, max_tests):
            return number
