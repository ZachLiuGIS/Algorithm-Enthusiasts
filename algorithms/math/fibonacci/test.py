import unittest
from fibonacci import fibonacci, fibonacci_with_mem

class FabonacciTest(unittest.TestCase):

    def test_fabonacci(self):
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(10), 55)

    def test_fabonacci_with_mem(self):
        self.assertEqual(fibonacci_with_mem(4), 3)
        self.assertEqual(fibonacci_with_mem(5), 5)
        self.assertEqual(fibonacci_with_mem(6), 8)
        self.assertEqual(fibonacci_with_mem(10), 55)
