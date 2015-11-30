import unittest
from Queue import Node, Queue


class QueueTest(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.queue.enqueue(5)

    def test_empty_queue(self):
        queue = Queue()
        self.assertEqual(queue.head, None)
        self.assertEqual(queue.tail, None)
        self.assertTrue(queue.is_empty())

        with self.assertRaises(Queue.Empty):
            queue.peek()

        with self.assertRaises(Queue.Empty):
            queue.dequeue()

    def test_size(self):
        self.assertEqual(self.queue.size(), 5)

    def test_enqueue(self):
        self.queue.enqueue(6)
        self.assertEqual(self.queue.size(), 6)
        self.assertEqual(self.queue.tail.get_data(), 6)

    def test_dequeue(self):
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)

    def test_peek(self):
        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(self.queue.peek(), 1)

