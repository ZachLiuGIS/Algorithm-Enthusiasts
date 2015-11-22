import unittest
import sys

DATA_STRUCTURE_DIR = '../..'
sys.path.append(DATA_STRUCTURE_DIR)

from partition import partition
from LinkedList import LinkedList


class ReturnKthToLastTest(unittest.TestCase):
    def setUp(self):
        self.default_list = LinkedList()
        self.default_list.insert(1)
        self.default_list.insert(2)
        self.default_list.insert(10)
        self.default_list.insert(5)
        self.default_list.insert(8)
        self.default_list.insert(5)
        self.default_list.insert(3)

    def test_partition(self):
        new_list = partition(self.default_list, 5)
        current = new_list.head
        self.assertTrue(current.get_data() < 5)
        current = current.get_next()
        self.assertTrue(current.get_data() < 5)
        current = current.get_next()
        self.assertTrue(current.get_data() < 5)
        current = current.get_next()
        self.assertTrue(current.get_data() >= 5)
        current = current.get_next()
        self.assertTrue(current.get_data() >= 5)
        current = current.get_next()
        self.assertTrue(current.get_data() >= 5)
