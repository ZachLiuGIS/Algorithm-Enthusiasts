import unittest
from PriorityQueue import MaxPQ, MinPQ


class MaxPQTest(unittest.TestCase):

    def setUp(self):
        self.pq = MaxPQ()
        for v in [6, 10, -2, 20, 9, 3, -8, 16, 11, 2]:
            self.pq.insert(v)

    def test_size(self):
        self.assertEqual(self.pq.size(), 10)

    def test_peek_max(self):
        self.assertEqual(self.pq.peek_max(), 20)
        self.assertEqual(self.pq.peek_max(), 20)

    def test_del_max(self):
        self.assertEqual(self.pq.del_max(), 20)
        self.assertEqual(self.pq.del_max(), 16)
        self.assertEqual(self.pq.del_max(), 11)


class MinPQTest(unittest.TestCase):

    def setUp(self):
        self.pq = MaxPQ()
        for v in [6, 10, -2, 20, 9, 3, -8, 16, 11, 2]:
            self.pq.insert(v)

    def test_size(self):
        self.assertEqual(self.pq.size(), 10)

    def test_peek_max(self):
        self.assertEqual(self.pq.peek_min(), -8)
        self.assertEqual(self.pq.peek_min(), -8)

    def test_del_max(self):
        self.assertEqual(self.pq.del_min(), -8)
        self.assertEqual(self.pq.del_min(), -2)
        self.assertEqual(self.pq.del_min(), 2)
