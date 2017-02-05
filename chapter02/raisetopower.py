def raise_to_power(x: float, y: int) -> float:
    """
    Возведение числа x в степень y.
    Raising a number x to the power y.
    """
    power = 1
    value_power = x
    power_values = {1: x}
    while power+1 <= y:
        power *= 2
        value_power *= value_power
        power_values[power] = value_power
    result = 1
    for power in sorted(power_values, reverse=True):
        if power <= y:
            result *= power_values[power]
            y -= power
            if y == 0:
                break
    return result
