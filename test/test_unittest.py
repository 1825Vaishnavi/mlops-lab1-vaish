import unittest
from src.calculator import fun1, fun2, fun3, fun4,fun5

class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(fun1(2, 3), 5)

    def test_fun2(self):
        self.assertEqual(fun2(5, 3), 2)

    def test_fun3(self):
        self.assertEqual(fun3(2, 4), 8)

    def test_fun4(self):
        self.assertEqual(fun4(2, 3), (2+3)+(2-3)+(2*3))

        def test_fun5(self):
            self.assertEqual(fun5(2, 3), 8)


if __name__ == "__main__":
    unittest.main()
