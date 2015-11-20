import unittest
from LinkedList import Node, LinkedList


class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.default_list = LinkedList()
        self.default_list.insert('a')
        self.default_list.insert('b')
        self.default_list.insert('c')
        self.default_list.insert('d')

    def test_insert(self):
        self.default_list.insert('z')
        self.assertEqual(self.default_list.head.get_data(), 'z')
        self.assertEqual(self.default_list.head.get_next().get_data(), 'd')

    def test_get_next(self):
        self.assertEqual(self.default_list.head.get_next().get_data(), 'c')

    def test_search(self):
        # search head
        self.assertEqual(self.default_list.search('d'), self.default_list.head)
        # normal search
        self.assertEqual(self.default_list.search('c'), self.default_list.head.get_next())
        # search value not in list
        with self.assertRaises(ValueError):
            self.default_list.search('e')

    def test_delete_head(self):
        self.default_list.delete('d')
        self.assertEqual(self.default_list.head.get_data(), 'c')
        self.assertEqual(self.default_list.size(), 3)

    def test_delete_tail(self):
        self.default_list.delete('a')
        self.assertEqual(self.default_list.size(), 3)

    def test_delete_not_exist(self):
        with self.assertRaises(ValueError):
            self.default_list.delete('e')

