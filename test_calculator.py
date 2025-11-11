import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add2(self):
        self.assertEqual(self.calc.add(-4, 3), -1)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(-1, 4), 5)

    def test_sub2(self):
        self.assertEqual(self.calc.subtract(1, -3), -4)

    def test_mul(self):
        self.assertEqual(self.calc.multiply(3, -4), -12)
    
    def test_mul2(self):
        self.assertEqual(self.calc.multiply(1, 0), 0)

    def test_div(self):
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_div2(self):
        self.assertEqual(self.calc.divide(-15, 5), -3)

    def test_mod(self):
        self.assertEqual(self.calc.modulo(25, -6), -5)

    def test_mod2(self):
        self.assertEqual(self.calc.modulo(11, 4), 3)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()