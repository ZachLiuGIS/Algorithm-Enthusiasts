import unittest
from two_sum import two_sum_brute_force, two_sum_dict, two_sum_sort

class TwoSumTest(unittest.TestCase):

    def setUp(self):
        self.arr = [3, 4, 7, 2, 9, 5]

    def test_brute_force(self):
        indices = two_sum_brute_force(self.arr, 6)
        self.assertEqual(indices[0], 2)
        self.assertEqual(indices[1], 4)

        indices = two_sum_brute_force(self.arr, 20)
        self.assertEqual(indices, None)

    def test_dict(self):
        indices = two_sum_dict(self.arr, 6)
        self.assertEqual(indices[0], 2)
        self.assertEqual(indices[1], 4)

        indices = two_sum_dict(self.arr, 20)
        self.assertEqual(indices, None)
