from unittest import TestCase

from chapter01.GCD import GCD


class TestGCD(TestCase):
    def test_GCD(self):
        tests = ((2835, 95985, 405), (3064, 47109, 383), (25047, 33143, 253),
                 (4164, 91608, 4164), (77316, 90202, 12886), (41492, 29520, 164),
                 (75750, 29400, 150), (5359, 68735, 233), (53788, 6664, 476),
                 (73399, 37965, 2531), (76024, 88322, 1118), (44, 22, 22))
        for a, b, result in tests:
            self.assertEqual(GCD(a, b), result)
