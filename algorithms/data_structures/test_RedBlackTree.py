from unittest import TestCase
from RedBlackTree import LeftLeanRedBlackTree


class LeftLeanRedBlackTreeTest(TestCase):

    def setUp(self):
        self.rbt = LeftLeanRedBlackTree()
        self.rbt.put('E', 10)
        self.rbt.put('A', 6)
        self.rbt.put('R', 2)
        self.rbt.put('C', 13)
        self.rbt.put('H', 1)
        self.rbt.put('X', -3)
        self.rbt.put('M', 0)
        self.rbt.put('P', 17)
        self.rbt.put('L', 5)

    def test_get(self):
        self.assertEqual(self.rbt.get('C'), 13)
        self.assertEqual(self.rbt.get('M'), 0)
        self.assertEqual(self.rbt.get('Z'), None)

    def test_size(self):
        self.assertEqual(self.rbt.size(), 9)
        self.rbt.put('Z', 10)
        self.assertEqual(self.rbt.size(), 10)

    def test_min(self):
        self.assertEqual(self.rbt.min(), 'A')

    def test_delete_min(self):
        self.rbt.delete_min()
        self.assertEqual(self.rbt.min(), 'C')

        self.rbt.delete_min()
        self.assertEqual(self.rbt.min(), 'E')

    def test_delete_max(self):
        self.rbt.delete_max()
        self.assertEqual(self.rbt.max(), 'C')

        self.rbt.delete_max()
        self.assertEqual(self.rbt.max(), 'E')

    def test_delete(self):
        self.assertEqual(self.rbt.get('C'), 13)
        self.rbt.delete('C')
        self.assertNotEqual(self.rbt.get('C'), 13)
        self.assertEqual(self.rbt.get('C'), None)

