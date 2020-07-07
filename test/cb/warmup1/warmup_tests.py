import unittest

from cb.warmup1.makes10 import makes10
from cb.warmup1.near_hundred import near_hundred


class TestCBWarmPp1(unittest.TestCase):
    def testMakes10(self):
        self.assertTrue(makes10(9, 10))
        self.assertFalse(makes10(9, 9))
        self.assertTrue(makes10(1, 9))

    def testNearHundred(self):
        self.assertTrue(near_hundred(93))
        self.assertTrue(near_hundred(90))
        self.assertFalse(near_hundred(89))


if __name__ == '__main__':
    unittest.main()
