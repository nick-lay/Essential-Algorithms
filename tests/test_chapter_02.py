import math
from unittest import TestCase

from chapter02.raisetopower import raise_to_power
from chapter02.findfactors import find_factors
from chapter02.findprimes import find_primes, find_prime, is_prime, _raise_to_power_by_module
from chapter02.numintegration import rectangle_rule, trapezoid_rule, adoptive_midpoint


def _some_function(x: float) -> float:
    return 1 + x + math.sin(2*x)


class TestChapter(TestCase):
    def test_raise_to_power(self):
        tests = [(65, 9, 20711912837890625),
                 (59, 3, 205379),
                 (62, 0, 1),
                 (40, 38, 7555786372591432341913600000000000000000000000000000000000000),
                 (26, 1, 26),
                 (84, 17, 516116642098754030145043477561344),
                 (35, 23, 326260892630588011062145233154296875),
                 (68, 40, 19969008794583656779033028746794280878790684292734333274333098048409829376),
                 (29, 27, 3053134545970524535745336759489912159909),
                 (88, 9, 316478381828866048)]
        for a, b, result in tests:
            self.assertEqual(result, raise_to_power(a, b))

    def test_find_factors(self):
        tests = ((664882073046, [2, 3, 3, 37, 389, 1597, 1607]),
                 (155157254555, [5, 2267, 13688333]),
                 (152510971152, [2, 2, 2, 2, 3, 3177311899]),
                 (130861948212, [2, 2, 3, 3, 3635054117]),
                 (919390834183, [919390834183]),
                 (354804858018, [2, 3, 3, 13, 35449, 42773]),
                 (617815993053, [3, 7, 31, 949026103]),
                 (691973791252, [2, 2, 197, 878139329]),
                 (413628737112, [2, 2, 2, 3, 3, 3, 5059, 378523]),
                 (226881403322, [2, 7, 16205814523]),
                 (9, [3, 3]),
                 (49, [7, 7]))
        for number, factors in tests:
            self.assertEqual(find_factors(number), factors)

    def test_find_primes(self):
        tests = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(find_primes(100), tests)

    def test_is_prime_pass(self):
        tests = [3, 23, 853, 3083, 14081, 848707, 3301391, 70922359, 660323933, 7689207079]
        for number in tests:
            self.assertTrue(is_prime(number))

    def test_is_prime_fail(self):
        tests = [9, 33, 629, 8786, 60162, 506117, 1081240, 10301550, 961657230, 5234003114]
        for number in tests:
            self.assertFalse(is_prime(number))

    def test_find_prime(self):
        for num_digits in range(1, 31):
            prime = find_prime(num_digits)
            self.assertTrue(is_prime(prime))

    def test_raise_to_power_by_module(self):
        tests = [((7, 29, 30), 7),
                 ((50, 80, 81), 34),
                 ((26, 92, 93), 25),
                 ((41, 47, 48), 41),
                 ((18, 90, 91), 64),
                 ((9, 55, 56), 9),
                 ((32, 38, 39), 10),
                 ((15, 21, 22), 15),
                 ((29, 38, 39), 22),
                 ((2, 13, 14), 2)]
        for param, result in tests:
            self.assertEqual(_raise_to_power_by_module(*param), result)

    def test_rectangle_rule(self):
        tests = [(_some_function, (0, 50, 100), 1287.6895973137248),
                 (_some_function, (0, 50, 1000), 1298.831442328184),
                 (_some_function, (0, 50, 10000), 1299.9451059043236),
                 (_some_function, (0, 50, 20000), 1300.0069733775213),
                 (_some_function, (0, 5, 100), 18.30736988476295)]
        for func, param, result in tests:
            self.assertEqual(rectangle_rule(func, *param), result)

    def test_trapezoid_rule(self):
        tests = [(_some_function, (0, 50, 100), 1300.063005903447),
                 (_some_function, (0, 50, 1000), 1300.0687831871567),
                 (_some_function, (0, 50, 10000), 1300.0688399902183),
                 (_some_function, (0, 50, 20000), 1300.0688404204705),
                 (_some_function, (0, 5, 100), 18.41876935699072)]
        for func, param, result in tests:
            self.assertEqual(trapezoid_rule(func, *param), result)

    def test_adoptive_midpoint(self):
        tests = [(_some_function, (0, 5, 3, 0.001), 18.418526233499527),
                 (_some_function, (0, 5, 5, 0.001), 18.41917031334151),
                 (_some_function, (0, 5, 10, 0.001), 18.41917031334151)]
        for func, param, result in tests:
            self.assertEqual(adoptive_midpoint(func, *param), result)
