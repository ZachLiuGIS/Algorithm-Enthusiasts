# Used to color the node
RED = True
BLACK = False


class LeftLeanRedBlackTree(object):

    class Node(object):

        def __init__(self, key, value, color, left=None, right=None, n=1):
            self.key = key
            self.value = value
            self.color = color
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

    def _is_red(self, node):
        if node is None:
            return False
        return node.color is RED

    def _rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = RED
        x.n = node.n
        node.n = self._size(node.left) + 1 + self._size(node.right)
        return x

    def _rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = RED
        x.n = node.n
        node.n = self._size(node.left) + 1 + self._size(node.right)
        return x

    def _move_red_left(self, node):
        self.flip_colors(node)

        if self._is_red(node.right.left):
            node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)
            self.flip_colors(node)

        return node

    def _move_red_right(self, node):
        self.flip_colors(node)

        if self._is_red(node.left.left):
            node = self._rotate_right(node)
            self.flip_colors(node)

        return node

    def flip_colors(self, node):
        node.color = not node.color
        node.left.color = not node.left.color
        node.right.color = not node.right.color

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
        root = self.root
        self.root = self._put(root, key, value)
        self.root.color = BLACK

    def _put(self, node, key, value):
        # insert at the bottom
        if node is None:
            return self.Node(key, value, RED)

        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value

        # fix right-leaning reds on the way up
        if self._is_red(node.right):
            node = self._rotate_left(node)

        # fix two reds in a row on the way up
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)

        # split 4-nodes
        if self._is_red(node.left) and self._is_red(node.right):
            self.flip_colors(node)

        node.n = self._size(node.left) + 1 + self._size(node.right)
        return node

    def min(self):
        root = self.root
        if root is not None:
            return self._min(root).key
        return None

    def _min(self, node):
        if node.left is None:
            return node
        return self._min(node.left)

    def max(self):
        root = self.root
        if root is not None:
            return self._max(root).key
        return None

    def _max(self, node):
        if node.right is None:
            return node
        return self._max(node.right)

    def delete_min(self):
        root = self.root
        if root is None:
            return

        if not self._is_red(root.left) and not self._is_red(root.right):
            self.root.color = RED

        self.root = self._delete_min(root)

        if not self.size() == 0:
            self.root.color = BLACK

    def _delete_min(self, node):
        if node.left is None:
            return None

        if not self._is_red(node.left) and not self._is_red(node.left.left):
            node = self._move_red_left(node)

        node.left = self._delete_min(node.left)

        return self._balance(node)

    def delete_max(self):
        root = self.root
        if root is None:
            return

        if not self._is_red(root.left) and not self._is_red(root.right):
            self.root.color = RED

        self.root = self._delete_max(root)

        if not self.size() == 0:
            self.root.color = BLACK

    def _delete_max(self, node):
        if self._is_red(node.left):
            node = self._rotate_right(node)

        if node.right is None:
            return None

        if not self._is_red(node.right) and not self._is_red(node.right.left):
            node = self._move_red_right(node)

        node.right = self._delete_max(node.right)

        return self._balance(node)

    def delete(self, key):
        root = self.root
        if root is None:
            return

        if not self._is_red(root.left) and not self._is_red(root.right):
            self.root.color = RED

        self.root = self._delete(root, key)

        if not self.size() == 0:
            self.root.color = BLACK

    def _delete(self, node, key):

        if key < node.key:
            if not self._is_red(node.left) and not self._is_red(node.left.left):
                node = self._move_red_left(node)
            node.left = self._delete(node.left, key)

        else:
            if self._is_red(node.left):
                node = self._rotate_right(node)
            if key == node.key and node.right is None:
                return None
            if not self._is_red(node.right) and not self._is_red(node.right.left):
                node = self._move_red_right(node)
            if key == node.key:
                x = self._min(node.right)
                node.key = x.key
                node.value = x.value
                node.right = self._delete_min(node.right)
            else:
                node.right = self._delete(node.right, key)
        return self._balance(node)

    def _balance(self, node):
        if self._is_red(node.right):
            node = self._rotate_left(node)

        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)

        if self._is_red(node.left) and self._is_red(node.right):
            self.flip_colors(node)

        node.n = self._size(node.left) + 1 + self._size(node.right)
        return node

    def print_in_order(self):
        root = self.root
        self._print_in_order(root)
        print()

    def _print_in_order(self, node):
        if node is None:
            return
        self._print_in_order(node.left)
        print(node.key + ':' + str(node.value), end=' ')
        self._print_in_order(node.right)


if __name__ == '__main__':
    rbt = LeftLeanRedBlackTree()

    rbt.put('E', 10)
    rbt.put('A', 6)
    rbt.put('R', 2)
    rbt.put('C', 13)
    rbt.put('H', 1)
    rbt.put('X', -3)
    rbt.put('M', 0)
    rbt.put('P', 17)
    rbt.put('L', 5)

    rbt.print_in_order()

    rbt.put('L', 15)
    rbt.print_in_order()

    print(rbt.get('E'))


