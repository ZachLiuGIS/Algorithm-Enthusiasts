import unittest
from Stack import Node, Stack


class StackTest(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(5)

    def test_empty_stack(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)

        with self.assertRaises(Stack.Empty):
            stack.peek()

        with self.assertRaises(Stack.Empty):
            stack.pop()

    def test_size(self):
        self.assertEqual(self.stack.size(), 5)

    def test_push(self):
        stack = self.stack
        self.assertEqual(stack.size(), 5)
        stack.push(6)
        self.assertEqual(stack.size(), 6)

    def test_peek(self):
        value = self.stack.peek()
        self.assertEqual(value, 5)
        value = self.stack.peek()
        self.assertEqual(value, 5)

    def test_pop(self):
        value = self.stack.pop()
        self.assertEqual(value, 5)
        value = self.stack.pop()
        self.assertEqual(value, 4)
