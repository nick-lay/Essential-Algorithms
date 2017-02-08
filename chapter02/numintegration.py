from typing import Callable


def rectangle_rule(func: Callable[[float], float], x_min: float, x_max: float, num_intervals: int) -> float:
    dx = (x_max-x_min) / num_intervals
    total_area = 0
    x = x_min
    for i in range(num_intervals):
        total_area += dx * func(x)
        x += dx
    return total_area
