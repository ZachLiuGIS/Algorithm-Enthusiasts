import unittest
import sys

DATA_STRUCTURE_DIR = '../..'
sys.path.append(DATA_STRUCTURE_DIR)

from LinkedList import LinkedList, Node
from check_loop import check_loop


class CheckPalindromeTest(unittest.TestCase):
    def setUp(self):
        self.lst1 = LinkedList()

        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node7 = Node(7)

        self.lst1.head = node1
        node1.set_next(node2)
        node2.set_next(node3)
        node3.set_next(node4)
        node4.set_next(node5)
        node5.set_next(node6)
        node6.set_next(node7)
        node7.set_next(node3)

        self.lst2 = LinkedList()
        self.lst2.insert(4)
        self.lst2.insert(3)
        self.lst2.insert(0)
        self.lst2.insert(7)
        self.lst2.insert(2)
        self.lst2.insert(3)
        self.lst2.insert(4)

    def test_check_loop(self):
        self.assertTrue(check_loop(self.lst1))
        self.assertFalse(check_loop(self.lst2))

