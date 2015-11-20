import unittest
import sys
DATA_STRUCTURE_DIR = '../..'
sys.path.append(DATA_STRUCTURE_DIR)

from get_kth_to_last import get_kth_to_last, get_kth_to_last_two_pointers, get_kth_to_last_reverse
from LinkedList import LinkedList


class ReturnKthToLastTest(unittest.TestCase):

    def setUp(self):

        self.default_list = LinkedList()
        self.default_list.insert('a')
        self.default_list.insert('b')
        self.default_list.insert('c')
        self.default_list.insert('d')
        self.default_list.insert('e')
        self.default_list.insert('f')

    def test_return_kth_to_last_recursive(self):
        head = self.default_list.head
        kth_to_last = get_kth_to_last(head, 2)
        self.assertTrue(kth_to_last.get_data(), 'b')

    def test_return_kth_to_last_two_pointers(self):
        head = self.default_list.head
        kth_to_last = get_kth_to_last_two_pointers(head, 2)
        self.assertTrue(kth_to_last.get_data(), 'b')

    def test_return_kth_to_last_reverse(self):
        head = self.default_list.head
        kth_to_last = get_kth_to_last_reverse(head, 2)
        self.assertTrue(kth_to_last.get_data(), 'b')
