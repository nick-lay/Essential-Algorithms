from typing import Callable


def rectangle_rule(func: Callable[[float], float], x_min: float, x_max: float, num_intervals: int) -> float:
    dx = (x_max-x_min) / num_intervals
    total_area = 0
    x = x_min
    for i in range(num_intervals):
        total_area += dx * func(x)
        x += dx
    return total_area


def trapezoid_rule(func: Callable[[float], float], x_min: float, x_max: float, num_intervals: int) -> float:
    dx = (x_max-x_min) / num_intervals
    total_area = 0
    x = x_min
    for i in range(num_intervals):
        total_area += dx * (func(x)+func(x+dx))/2
        x += dx
    return total_area


def _slice_area(func: Callable[[float], float], x1: float, x2: float, max_slice_error: float) -> float:
    y1 = func(x1)
    y2 = func(x2)
    xm = (x1+x2)/2
    ym = func(xm)
    area_12 = (x2-x1) * (y2+y1) / 2
    area_1m = (xm-x1) * (y1+ym) / 2
    area_m2 = (x2-xm) * (ym+y2) / 2
    area_1m2 = area_1m + area_m2
    error = (area_1m2-area_12) / area_12
    if abs(error) < max_slice_error:
        return area_1m2
    return _slice_area(func, x1, xm, max_slice_error) + _slice_area(func, xm, x2, max_slice_error)


def adoptive_midpoint(func: Callable[[float], float], x_min: float, x_max: float,
                      num_intervals: int, max_slice_error: float) -> float:
    dx = (x_max-x_min) / num_intervals
    total_area = 0
    x = x_min
    for i in range(num_intervals):
        total_area += _slice_area(func, x, x+dx, max_slice_error)
        x += dx
    return total_area
