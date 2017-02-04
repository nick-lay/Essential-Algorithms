def GCD(a: int, b: int) -> int:
    """
    Найти наибольший общий делитель(НОД) для двух целых чисел.
    Find greatest common divisor. (GCD)
    """
    while b:
        a, b = b, a % b
    return a
