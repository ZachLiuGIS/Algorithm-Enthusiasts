import unittest
import sys

DATA_STRUCTURE_DIR = '../..'
sys.path.append(DATA_STRUCTURE_DIR)

from LinkedList import LinkedList
from add_two_numbers import list_to_num, num_to_list, add_two_numbers, \
    list_to_num_reverse, num_to_list_reverse, add_two_numbers_reverse


class AddTwoNumbersTest(unittest.TestCase):
    def setUp(self):
        self.lst1 = LinkedList()
        self.lst2 = LinkedList()

        self.lst1.insert(4)
        self.lst1.insert(4)
        self.lst1.insert(3)
        self.lst2.insert(7)
        self.lst2.insert(5)
        self.lst2.insert(2)

    def test_list_to_num(self):
        self.assertEqual(list_to_num(self.lst1), 344)
        self.assertEqual(list_to_num(self.lst2), 257)

    def test_num_to_list(self):
        lst1 = num_to_list(344)
        self.assertEqual(lst1.head.get_data(), 3)

    def test_add_two_numbers(self):
        total = add_two_numbers(self.lst1, self.lst2)
        self.lst1.print()
        self.lst2.print()
        total.print()
        current = total.head
        self.assertEqual(current.get_data(), 6)
        current = current.get_next()
        self.assertEqual(current.get_data(), 0)
        current = current.get_next()
        self.assertEqual(current.get_data(), 1)

    def test_list_to_num_reverse(self):
        self.assertEqual(list_to_num_reverse(self.lst1), 443)
        self.assertEqual(list_to_num_reverse(self.lst2), 752)

    def test_num_to_list_reverse(self):
        lst1 = num_to_list_reverse(344)
        self.assertEqual(lst1.head.get_data(), 4)

    def test_add_two_numbers_reverse(self):
        total = add_two_numbers_reverse(self.lst1, self.lst2)
        self.lst1.print()
        self.lst2.print()
        total.print()
        current = total.head
        self.assertEqual(current.get_data(), 5)
        current = current.get_next()
        self.assertEqual(current.get_data(), 9)
        current = current.get_next()
        self.assertEqual(current.get_data(), 1)
