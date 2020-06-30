import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


class TestMakes10(unittest.TestCase):
    def test_makes10(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
