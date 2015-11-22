import unittest
import sys

DATA_STRUCTURE_DIR = '../..'
sys.path.append(DATA_STRUCTURE_DIR)

from find_intersection import find_intersection
from LinkedList import LinkedList


class FindIntersectionTest(unittest.TestCase):
    def setUp(self):
        self.lst1 = LinkedList()
        self.lst2 = LinkedList()
        self.common_lst = LinkedList()

        self.lst1.insert(4)
        self.lst1.insert(2)
        self.lst1.insert(5)
        self.lst1.insert(8)
        self.lst1.insert(6)

        self.lst2.insert(3)
        self.lst2.insert(10)
        self.lst2.insert(8)

        self.common_lst.insert(3)
        self.common_lst.insert(2)
        self.common_lst.insert(5)
        self.common_lst.insert(7)

        current = self.lst1.head
        while current.get_next():
            current = current.get_next()
        current.set_next(self.common_lst.head)

        current = self.lst2.head
        while current.get_next():
            current = current.get_next()
        current.set_next(self.common_lst.head)

    def test_find_intersection(self):
        lst = find_intersection(self.lst1, self.lst2)
        self.assertEqual(lst.size(), 4)
        self.assertEqual(lst.head.get_data(), 7)
        self.assertEqual(lst.head.get_next().get_data(), 5)

    def test_find_intersection_no_common(self):
        lst1 = LinkedList()
        lst2 = LinkedList()
        lst1.insert(4)
        lst1.insert(3)
        lst1.insert(2)
        lst1.insert(1)

        lst2.insert(4)
        lst2.insert(3)
        lst2.insert(2)

        lst = find_intersection(lst1, lst2)
        self.assertEqual(lst, None)
