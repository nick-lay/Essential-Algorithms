from unittest import TestCase

from chapter02.raisetopower import raise_to_power
from chapter02.findfactors import find_factors
from chapter02.findprimes import find_primes


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
                 (226881403322, [2, 7, 16205814523]))
        for number, factors in tests:
            self.assertEqual(find_factors(number), factors)

    def test_find_primes(self):
        tests = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(find_primes(100), tests)
