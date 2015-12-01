import unittest
import sys

DATA_STRUCTURE_DIR = '../..'
sys.path.append(DATA_STRUCTURE_DIR)

from Stack import Stack
from stack_min import StackWithMin


class StackWithMinTest(unittest.TestCase):

    def test_empty_stack(self):
        stack = StackWithMin()

        self.assertTrue(stack.is_empty())

        with self.assertRaises(Stack.Empty):
            stack.pop()

        with self.assertRaises(Stack.Empty):
            stack.peek()

        with self.assertRaises(Stack.Empty):
            stack.min()

    def test_push_and_pop(self):
        stack = StackWithMin()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)

    def test_min(self):
        stack = StackWithMin()
        stack.push(3)
        stack.push(2)
        stack.push(1)
        self.assertEqual(stack.min(), 1)
        stack.pop()
        self.assertEqual(stack.min(), 2)
        stack.pop()
        self.assertEqual(stack.min(), 3)
