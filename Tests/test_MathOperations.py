import unittest
from MathOperations.addition import Addition
from MathOperations.substraction import Substraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.mean import Mean


class MyTestCase(unittest.TestCase):

    def test_addition(self):
        result = Addition.sum(1, 2)
        self.assertEqual(3, result)

    def test_substraction(self):
        self.assertEqual(-1, Substraction.difference(1, 2))

    def test_multiplication(self):
        self.assertEqual(2, Multiplication.multiplication(1, 2))

    def test_divison(self):
        self.assertEqual(2, Division.quotient(10, 5))

    def test_mean(self):
        self.assertEqual(4, Mean.mean([4,4,4,4]))

if __name__ == '__main__':
    unittest.main()
