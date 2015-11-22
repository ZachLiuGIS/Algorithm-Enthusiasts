import sys

DATA_STRUCTURE_DIR = '../..'
sys.path.append(DATA_STRUCTURE_DIR)

from LinkedList import LinkedList


def partition(lst, value):
    below_lst = LinkedList()
    above_lst = LinkedList()

    current = lst.head

    while current:
        data = current.get_data()
        if data < value:
            below_lst.insert(data)
        else:
            above_lst.insert(data)
        current = current.get_next()

    # all node data is above value
    if below_lst.head is None:
        return above_lst
    else:
        current = below_lst.head
        while current.get_next():
            current = current.get_next()
        current.set_next(above_lst.head)

    return below_lst


if __name__ == '__main__':
    lst = LinkedList()
    lst.insert(1)
    lst.insert(2)
    lst.insert(10)
    lst.insert(5)
    lst.insert(8)
    lst.insert(5)
    lst.insert(3)

    new_lst = partition(lst, 5)
    new_lst.print()

