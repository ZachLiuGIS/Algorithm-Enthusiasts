import sys

DATA_STRUCTURE_DIR = '../..'
sys.path.append(DATA_STRUCTURE_DIR)

from LinkedList import LinkedList


def reverse_list(lst):
    new_lst = LinkedList()
    current = lst.head
    while current:
        new_lst.insert(current.get_data())
        current = current.get_next()
    return new_lst


def check_palindrome(lst):
    lst2 = reverse_list(lst)
    current_1 = lst.head
    current_2 = lst2.head

    length = lst.size()

    for i in range(int(length / 2)):
        if not current_1.get_data() == current_2.get_data():
            return False
        current_1 = current_1.get_next()
        current_2 = current_2.get_next()
    return True
