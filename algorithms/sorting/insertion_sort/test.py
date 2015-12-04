import unittest
from insertion_sort import insertion_sort


class BubbleSortTest(unittest.TestCase):

    def test_insertion_sort(self):
        lst1 = [1, 2, 3, 4, 5]
        lst1 = insertion_sort(lst1)
        self.assertEqual(lst1, [1, 2, 3, 4, 5])

        lst2 = [5, 4, 3, 2, 1]
        lst2 = insertion_sort(lst2)
        self.assertEqual(lst2, [1, 2, 3, 4, 5])

        lst3 = [2, 4, 3, 4, 5, 5, 1]
        lst3 = insertion_sort(lst3)
        self.assertEqual(lst3, [1, 2, 3, 4, 4, 5, 5])