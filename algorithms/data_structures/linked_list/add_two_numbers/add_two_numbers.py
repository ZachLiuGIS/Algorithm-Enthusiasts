import sys

DATA_STRUCTURE_DIR = '../..'
sys.path.append(DATA_STRUCTURE_DIR)

from LinkedList import LinkedList


def list_to_num(lst):
    current = lst.head
    num = current.get_data()
    current = current.get_next()
    while current:
        num = num * 10 + current.get_data()
        current = current.get_next()
    return num


def num_to_list(num):
    lst = LinkedList()

    if num == 0:
        lst.insert(0)
        return lst

    while num > 0:
        digit = num % 10
        lst.insert(digit)
        num = int(num / 10)

    return lst


def list_to_num_reverse(lst):
    head = lst.head
    num = head.get_data()
    digit = 1
    current = head.get_next()
    while current:
        num += current.get_data() * (10 ** digit)
        digit += 1
        current = current.get_next()
    return num


def num_to_list_reverse(num):
    lst = LinkedList()
    if num == 0:
        lst.insert(0)
        return lst

    arr = []
    while num > 0:
        digit = num % 10
        arr.append(digit)
        num = int(num / 10)
    arr.reverse()
    for digit in arr:
        lst.insert(digit)
    return lst


def add_two_numbers(lst1, lst2):
    num1 = list_to_num(lst1)
    num2 = list_to_num(lst2)
    total = num1 + num2
    lst = num_to_list(total)
    return lst


def add_two_numbers_reverse(lst1, lst2):
    num1 = list_to_num_reverse(lst1)
    num2 = list_to_num_reverse(lst2)
    total = num1 + num2
    lst = num_to_list_reverse(total)
    return lst


if __name__ == '__main__':
    lst1 = LinkedList()

    lst1.insert(4)
    lst1.insert(4)
    lst1.insert(3)
    print(list_to_num(lst1))

