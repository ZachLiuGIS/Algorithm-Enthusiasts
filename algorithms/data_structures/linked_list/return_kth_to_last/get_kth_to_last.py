import sys
DATA_STRUCTURE_DIR = '../..'
sys.path.append(DATA_STRUCTURE_DIR)

from LinkedList import LinkedList


def get_kth_to_last(head, k):

    node = None

    def get_kth_recurse(head_node, n):
        nonlocal node

        if head_node is None:
            return 0

        index = get_kth_recurse(head_node.get_next(), n) + 1

        if index == n:
            node = head_node

        return index

    get_kth_recurse(head, k)

    return node


def get_kth_to_last_two_pointers(head, k):
    p1 = p2 = head

    for i in range(k):
        p2 = p2.get_next()
        if p2 is None:
            return None

    while p2 is not None:
        p1 = p1.get_next()
        p2 = p2.get_next()
    return p1


def get_kth_to_last_reverse(head, k):
    lst = LinkedList()
    current = head
    while current:
        lst.insert(current.get_data())
        current = current.get_next()

    current = lst.head
    for i in range(k-1):
        current = current.get_next()
        if current is None:
            return None

    return current


if __name__ == '__main__':
    lst = LinkedList()
    lst.insert('a')
    lst.insert('b')
    lst.insert('c')
    lst.insert('d')
    lst.insert('e')
    lst.insert('f')

    head = lst.head

    print(get_kth_to_last(head, 2).get_data())
    print(get_kth_to_last(head, 12))

    print(get_kth_to_last_two_pointers(head, 2).get_data())
    print(get_kth_to_last_two_pointers(head, 12))

    print(get_kth_to_last_reverse(head, 2).get_data())
    print(get_kth_to_last_reverse(head, 12))
