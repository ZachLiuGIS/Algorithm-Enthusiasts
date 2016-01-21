class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_value(lst, node):
    if node is None:
        return
    get_value(lst, node.left)
    lst.append(node.val)
    get_value(lst, node.right)


def in_order_traversal_recursive(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    lst = []
    get_value(lst, root)
    return lst


def in_order_traversal(root):
    res = []
    stack = []
    node = root
    while stack or node is not None:
        if node:
            stack.append(node)
            node = node.left
        else:
            stack_node = stack.pop()
            res.append(stack_node.val)
            node = stack_node.right
    print(res)
    return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(in_order_traversal_recursive(root))

    assert in_order_traversal_recursive(root) == [3, 2, 4, 1, 6, 5, 7]
    assert in_order_traversal(root) == [3, 2, 4, 1, 6, 5, 7]
