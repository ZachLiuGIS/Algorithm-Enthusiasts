import unittest
import sys

DATA_STRUCTURE_DIR = '../..'
sys.path.append(DATA_STRUCTURE_DIR)

from Stack import Stack
from sort_stack import sort_stack


class SortStackTest(unittest.TestCase):

    def test_sort_stack(self):
        stack = Stack()
        stack.push(4)
        stack.push(5)
        stack.push(2)
        stack.push(7)

        sorted_stack = sort_stack(stack)
        self.assertEqual(sorted_stack.pop(), 2)
        self.assertEqual(sorted_stack.pop(), 4)
        self.assertEqual(sorted_stack.pop(), 5)
        self.assertEqual(sorted_stack.pop(), 7)
