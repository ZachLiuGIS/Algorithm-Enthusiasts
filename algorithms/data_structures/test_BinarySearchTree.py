from unittest import TestCase
from BinarySearchTree import BinarySearchTree


class BinarySearchTreeTest(TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()
        self.bst.put('H', 5)
        self.bst.put('B', 4)
        self.bst.put('K', 9)
        self.bst.put('C', 2)
        self.bst.put('I', -1)
        self.bst.put('M', 11)

    def test_get(self):
        self.assertEqual(self.bst.get('C'), 2)
        self.assertEqual(self.bst.get('M'), 11)
        self.assertEqual(self.bst.get('Z'), None)

    def test_size(self):
        self.assertEqual(self.bst.size(), 6)

    def test_min(self):
        self.assertEqual(self.bst.min(), 'B')

    def test_max(self):
        self.assertEqual(self.bst.max(), 'M')

    def test_floor(self):
        self.assertEqual(self.bst.floor('D'), 'C')
        self.assertEqual(self.bst.floor('M'), 'M')
        self.assertEqual(self.bst.floor('A'), None)

    def test_select(self):
        self.assertEqual(self.bst.select(0), 'B')
        self.assertEqual(self.bst.select(1), 'C')
        self.assertEqual(self.bst.select(5), 'M')
        self.assertEqual(self.bst.select(6), None)

    def test_rank(self):
        self.assertEqual(self.bst.rank('B'), 0)
        self.assertEqual(self.bst.rank('C'), 1)
        self.assertEqual(self.bst.rank('D'), 2)
        self.assertEqual(self.bst.rank('H'), 2)
        self.assertEqual(self.bst.rank('M'), 5)
        self.assertEqual(self.bst.rank('Z'), 6)

    def test_delete_min(self):
        self.bst.delete_min()
        self.assertEqual(self.bst.size(), 5)
        self.assertEqual(self.bst.min(), 'C')

    def test_delete(self):
        self.bst.delete('H')
        self.assertEqual(self.bst.size(), 5)
        self.assertEqual(self.bst.get('H'), None)

    def test_keys(self):
        keys = self.bst.keys('C', 'J')
        self.assertEqual(keys, ['C', 'H', 'I'])
