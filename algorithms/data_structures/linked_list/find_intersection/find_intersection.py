import sys

DATA_STRUCTURE_DIR = '../..'
sys.path.append(DATA_STRUCTURE_DIR)

from LinkedList import LinkedList


def find_intersection(lst1, lst2):

    current_lst1 = lst1.head
    current_lst2 = lst2.head

    count_lst1 = 1
    count_lst2 = 1

    while current_lst1.get_next():
        count_lst1 += 1
        current_lst1 = current_lst1.get_next()

    while current_lst2.get_next():
        count_lst2 += 1
        current_lst2 = current_lst2.get_next()

    if not current_lst1 == current_lst2:
        return None

    else:
        diff = lst1.size() - lst2.size()

        if diff > 0:
            pt = lst1.head
            for i in range(diff):
                pt = pt.get_next()
            lst1.head = pt

        elif diff < 0:
            pt = lst2.head
            for i in range(abs(diff)):
                pt = pt.get_next()
            lst2.head = pt

        current_lst1 = lst1.head
        current_lst2 = lst2.head

        while not current_lst1 == current_lst2:
            current_lst1 = current_lst1.get_next()
            current_lst2 = current_lst2.get_next()

        return_lst = LinkedList()
        return_lst.head = current_lst1
        return return_lst
