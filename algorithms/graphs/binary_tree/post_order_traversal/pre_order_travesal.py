class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_value(lst, node):
    if node is None:
        return
    get_value(lst, node.left)
    get_value(lst, node.right)
    lst.append(node.val)


def post_order_traversal_recursive(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    lst = []
    get_value(lst, root)
    return lst


def post_order_traversal(root):
    res = []
    if root is None:
        return res
    stack = []
    if root.right:
        stack.append(root.right)
    if root.left:
        stack.append(root.left)
    stack.append(root)

    while stack:
        node = stack.pop()
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
        res.append(root.val)

    return res


def post_order_traversal2(root):
    res = []
    stack = []
    node = root
    while stack or node is not None:
        if node:
            stack.append(node)
            res.append(node.val)
            node = node.right
        else:
            stack_node = stack.pop()
            node = stack_node.left
    return res[::-1]


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(post_order_traversal_recursive(root))

    assert post_order_traversal_recursive(root) == [3, 4, 2, 6, 7, 5, 1]
    # assert post_order_traversal(root) == [3, 4, 2, 6, 7, 5, 1]
    assert post_order_traversal2(root) == [3, 4, 2, 6, 7, 5, 1]
