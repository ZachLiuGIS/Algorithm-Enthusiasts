import unittest
from book_pricing import simple_price, price


# Some of these tests will fail because the issue with this naive solution
class SimplePriceTest(unittest.TestCase):

    def test_basics(self):
        self.assertEqual(0, simple_price([]))
        self.assertEqual(8, simple_price([0]))
        self.assertEqual(8, simple_price([1]))
        self.assertEqual(8, simple_price([2]))
        self.assertEqual(8, simple_price([3]))
        self.assertEqual(8, simple_price([4]))
        self.assertEqual(8 * 2, simple_price([0, 0]))
        self.assertEqual(8 * 3, simple_price([1, 1, 1]))

    def testSimpleDiscounts(self):
        self.assertEqual(8 * 2 * 0.95, simple_price([0, 1]))
        self.assertEqual(8 * 3 * 0.9, simple_price([0, 2, 4]))
        self.assertEqual(8 * 4 * 0.8, simple_price([0, 1, 2, 4]))
        self.assertEqual(8 * 5 * 0.75, simple_price([0, 1, 2, 3, 4]))

    def testSeveralDiscounts(self):
        self.assertEqual(8 + (8 * 2 * 0.95), simple_price([0, 0, 1]))
        self.assertEqual(2 * (8 * 2 * 0.95), simple_price([0, 0, 1, 1]))
        self.assertEqual((8 * 4 * 0.8) + (8 * 2 * 0.95), simple_price([0, 0, 1, 2, 2, 3]))
        self.assertEqual(8 + (8 * 5 * 0.75), simple_price([0, 1, 1, 2, 3, 4]))

    # this one will fail
    def testEdgeCases(self):
        self.assertEqual(2 * (8 * 4 * 0.8), simple_price([0, 0, 1, 1, 2, 2, 3, 4]))
        self.assertEqual(3 * (8 * 5 * 0.75) + 2 * (8 * 4 * 0.8),
            simple_price([0, 0, 0, 0, 0,
                   1, 1, 1, 1, 1,
                   2, 2, 2, 2,
                   3, 3, 3, 3, 3,
                   4, 4, 4, 4]))


# These tests should all pass
class PriceTest(unittest.TestCase):

    def test_basics(self):
        self.assertEqual(0, price([]))
        self.assertEqual(8, price([0]))
        self.assertEqual(8, price([1]))
        self.assertEqual(8, price([2]))
        self.assertEqual(8, price([3]))
        self.assertEqual(8, price([4]))
        self.assertEqual(8 * 2, price([0, 0]))
        self.assertEqual(8 * 3, price([1, 1, 1]))

    def testSimpleDiscounts(self):
        self.assertEqual(8 * 2 * 0.95, price([0, 1]))
        self.assertEqual(8 * 3 * 0.9, price([0, 2, 4]))
        self.assertEqual(8 * 4 * 0.8, price([0, 1, 2, 4]))
        self.assertEqual(8 * 5 * 0.75, price([0, 1, 2, 3, 4]))

    def testSeveralDiscounts(self):
        self.assertEqual(8 + (8 * 2 * 0.95), price([0, 0, 1]))
        self.assertEqual(2 * (8 * 2 * 0.95), price([0, 0, 1, 1]))
        self.assertEqual((8 * 4 * 0.8) + (8 * 2 * 0.95), price([0, 0, 1, 2, 2, 3]))
        self.assertEqual(8 + (8 * 5 * 0.75), price([0, 1, 1, 2, 3, 4]))

    def testEdgeCases(self):
        self.assertEqual(2 * (8 * 4 * 0.8), price([0, 0, 1, 1, 2, 2, 3, 4]))
        self.assertEqual(3 * (8 * 5 * 0.75) + 2 * (8 * 4 * 0.8),
            price([0, 0, 0, 0, 0,
                   1, 1, 1, 1, 1,
                   2, 2, 2, 2,
                   3, 3, 3, 3, 3,
                   4, 4, 4, 4]))


if __name__ == '__main__':
    unittest.main()
