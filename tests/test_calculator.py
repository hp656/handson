import unittest
from src.calculator import add, subtract, divide 
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(1, -1), 2)

    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)
        self.assertEqual(divide(-2 , 2), -1)
        self.assertEqual(divide(-2, -2), 1)
   
if __name__ == '__main__':
   unittest.main()