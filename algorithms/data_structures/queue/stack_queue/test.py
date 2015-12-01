import unittest
import sys

DATA_STRUCTURE_DIR = '../..'
sys.path.append(DATA_STRUCTURE_DIR)

from Stack import Stack
from StackQueue import StackQueue


class StackQueueTest(unittest.TestCase):

    def test_empty_queue(self):
        queue = StackQueue()
        self.assertTrue(queue.is_empty())

        with self.assertRaises(StackQueue.Empty):
            queue.dequeue()

        with self.assertRaises(StackQueue.Empty):
            queue.peek()

    def test_enqueue_dequeue(self):
        queue = StackQueue()
        queue.enqueue(1)
        queue.enqueue(2)

        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)

        with self.assertRaises(StackQueue.Empty):
            queue.dequeue()

    def test_peek(self):
        queue = StackQueue()
        queue.enqueue(1)
        queue.enqueue(2)

        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.peek(), 1)