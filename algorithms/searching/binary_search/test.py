import unittest
from binary_search import binary_search

class BinarySearchTest(unittest.TestCase):

    def test_binary_search(self):
        arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        arr2 = [1, 3, 5, 7, 9, 11, 13, 15, 17]
        arr3 = [2, 4, 6, 8, 10, 12, 14, 16, 18]

        self.assertEqual(binary_search(arr1, 5), 4)
        self.assertEqual(binary_search(arr2, 10), False)
        self.assertEqual(binary_search(arr3, 16), 7)