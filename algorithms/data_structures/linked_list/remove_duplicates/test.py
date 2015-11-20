import unittest
import sys
import os
DATA_STRUCTURE_DIR = '../..'
sys.path.append(DATA_STRUCTURE_DIR)

from remove_duplicates import remove_duplicates
from LinkedList import LinkedList


class RemoveDuplicatesTest(unittest.TestCase):

    def setUp(self):
        self.default_list = LinkedList()
        self.default_list.insert('a')
        self.default_list.insert('b')
        self.default_list.insert('c')
        self.default_list.insert('c')
        self.default_list.insert('d')
        self.default_list.insert('d')

    def test_remove_duplicates(self):
        remove_duplicates(self.default_list)
        self.assertEqual(self.default_list.size(), 4)
