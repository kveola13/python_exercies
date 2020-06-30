import unittest

from cb.warmup1.parrot_trouble import parrot_trouble


class TestParrotTrouble(unittest.TestCase):
    def test_parrot_trouble(self):
        self.assertTrue(parrot_trouble(True, 3))


if __name__ == '__main__':
    unittest.main()
