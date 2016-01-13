class BinarySearchTree(object):

    class Node(object):

        def __init__(self, key, value, left=None, right=None, n=1):
            self.key = key
            self.value = value
            self.left = left
            self.right = right
            self.n = n

    def __init__(self):
        self.root = None

    def size(self):
        root = self.root
        return self._size(root)

    def _size(self, node):
        if node is None:
            return 0
        return node.n

    def get(self, key):
        root = self.root
        return self._get(root, key)

    def _get(self, node, key):
        if node is None:
            return None

        if node.key == key:
            return node.value
        elif node.key < key:
            return self._get(node.right, key)
        else:
            return self._get(node.left, key)

    def put(self, key, value):
        self.root = self._put(self.root, key, value)

    def _put(self, node, key, value):
        if node is None:
            return self.Node(key, value)

        if node.key == key:
            node.value = value
        elif node.key < key:
            node.right = self._put(node.right, key, value)
        else:
            node.left = self._put(node.left, key, value)

        node.n = self._size(node.left) + self._size(node.right) + 1

        return node

    def min(self):
        root = self.root
        min_ = self._min(root)
        if min_:
            return min_.key
        return None

    def _min(self, node):
        if node.left is None:
            return node
        return self._min(node.left)

    def max(self):
        root = self.root
        max_ = self._max(root)
        if max_:
            return max_.key
        return None

    def _max(self, node):
        if node.right is None:
            return node
        return self._max(node.right)

    def floor(self, key):
        root = self.root
        node = self._floor(root, key)
        if node:
            return node.key
        return None

    def _floor(self, node, key):
        if node is None:
            return None

        if node.key == key:
            return node
        elif key < node.key:
            return self._floor(node.left, key)
        else:
            t = self._floor(node.right, key)
            if t is None:
                return node
            return t

    def select(self, rank):
        root = self.root
        node = self._select(root, rank)
        if node:
            return node.key
        return None

    def _select(self, node, rank):
        if node is None:
            return None

        size = self._size(node.left)
        if size == rank:
            return node
        elif size > rank:
            return self._select(node.left, rank)
        else:
            return self._select(node.right, rank - size - 1)

    def rank(self, key):
        root = self.root
        return self._rank(root, key)

    def _rank(self, node, key):
        if node is None:
            return 0

        if key == node.key:
            return self._size(node.left)
        elif key < node.key:
            return self._rank(node.left, key)
        else:
            return self._size(node.left) + 1 + self._rank(node.right, key)

    def delete_min(self):
        root = self.root
        self.root = self._delete_min(root)

    def _delete_min(self, node):
        if node.left is None:
            return node.right
        node.left = self._delete_min(node.left)
        node.n = self._size(node.left) + 1 + self._size(node.right)
        return node

    def delete(self, key):
        root = self.root
        self.root = self._delete(root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.left
            elif node.right is None:
                return node.left
            else:
                t = node
                node = self._min(t.right)
                node.right = self._delete_min(t.right)
                node.left = t.left
        node.n = self._size(node.left) + 1 + self._size(node.right)
        return node

    def keys(self, lo, hi):
        keys = []
        root = self.root
        self._keys(root, keys, lo, hi)
        return keys

    def _keys(self, node, keys, lo, hi):
        if node is None:
            return None
        if node.key > lo:
            self._keys(node.left, keys, lo, hi)
        if lo <= node.key <= hi:
            keys.append(node.key)
        if node.key < hi:
            self._keys(node.right, keys, lo, hi)

    def print_in_order(self):
        root = self.root
        self._print_in_order(root)

    def _print_in_order(self, node):
        if node is None:
            return
        self._print_in_order(node.left)
        print(node.key, end=' ')
        self._print_in_order(node.right)


if __name__ == '__main__':
    bst = BinarySearchTree()

    print(bst.size())
    bst.put('C', 10)
    bst.put('A', 6)
    bst.put('D', 2)

    bst.print_in_order()
    print(bst.get('C'))
    print(bst.get('B'))
    print(bst.min())
    print(bst.max())
    print(bst.floor('B'))
    print(bst.select(1))
    print(bst.rank('H'))

    bst.put('B', 5)
    bst.print_in_order()
    bst.delete_min()
    print()
    bst.print_in_order()

    bst.delete('C')
    print()
    bst.print_in_order()

    print(bst.keys('C', 'I'))
