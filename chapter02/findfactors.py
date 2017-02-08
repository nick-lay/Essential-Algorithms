import math
from typing import List


def find_factors(number: int) -> List[int]:
    """
    Нахождение простых множителей.
    Find Prime factors.
    """
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number //= 2
    factor = 3
    max_factor = math.sqrt(number)
    while factor <= max_factor:
        while number % factor == 0:
            factors.append(factor)
            number //= factor
            max_factor = math.sqrt(number)
        factor += 2
    if number > 1:
        factors.append(number)

    return factors
