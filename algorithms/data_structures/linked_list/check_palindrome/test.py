import unittest
import sys

DATA_STRUCTURE_DIR = '../..'
sys.path.append(DATA_STRUCTURE_DIR)

from LinkedList import LinkedList
from check_palindrome import check_palindrome


class CheckPalindromeTest(unittest.TestCase):
    def setUp(self):
        self.lst1 = LinkedList()

        self.lst1.insert(4)
        self.lst1.insert(3)
        self.lst1.insert(0)
        self.lst1.insert(7)
        self.lst1.insert(0)
        self.lst1.insert(3)
        self.lst1.insert(4)

        self.lst2 = LinkedList()

        self.lst2.insert(4)
        self.lst2.insert(3)
        self.lst2.insert(0)
        self.lst2.insert(7)
        self.lst2.insert(2)
        self.lst2.insert(3)
        self.lst2.insert(4)

        self.lst3 = LinkedList()

        self.lst3.insert(4)
        self.lst3.insert(3)
        self.lst3.insert(0)
        self.lst3.insert(0)
        self.lst3.insert(3)
        self.lst3.insert(4)

        self.lst4 = LinkedList()

        self.lst4.insert(4)
        self.lst4.insert(1)
        self.lst4.insert(0)
        self.lst4.insert(0)
        self.lst4.insert(3)
        self.lst4.insert(4)

    def test_check_odd_num_nodes(self):
        self.assertTrue(check_palindrome(self.lst1))
        self.assertFalse(check_palindrome(self.lst2))

    def test_check_even_num_nodes(self):
        self.assertTrue(check_palindrome(self.lst3))
        self.assertFalse(check_palindrome(self.lst4))
