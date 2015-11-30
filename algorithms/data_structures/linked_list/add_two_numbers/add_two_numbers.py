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


def reverse_list(lst):
    new_lst = LinkedList()
    current = lst.head
    while current:
        new_lst.insert(current.get_data())
        current = current.get_next()
    return new_lst


def add_two_numbers_adding_digit_reverse(lst1, lst2):
    lst = LinkedList()
    current_1 = lst1.head
    current_2 = lst2.head
    carry = 0

    def get_digit(node1, node2):
        nonlocal carry
        num1 = 0 if node1 is None else node1.get_data()
        num2 = 0 if node2 is None else node2.get_data()
        value = num1 + num2 + carry
        if value >= 10:
            carry = 1
            value %= 10
        else:
            carry = 0
        return value

    current_lst = lst.head

    while current_1 is not None or current_2 is not None or carry > 0:
        digit = get_digit(current_1, current_2)
        lst.insert(digit)
        current_1 = current_1.get_next() if current_1 is not None else None
        current_2 = current_2.get_next() if current_2 is not None else None
    return reverse_list(lst)


def add_two_numbers_adding_digit(lst1, lst2):
    lst1 = reverse_list(lst1)
    lst2 = reverse_list(lst2)
    lst = LinkedList()
    current_1 = lst1.head
    current_2 = lst2.head
    carry = 0

    def get_digit(node1, node2):
        nonlocal carry
        num1 = 0 if node1 is None else node1.get_data()
        num2 = 0 if node2 is None else node2.get_data()
        value = num1 + num2 + carry
        if value >= 10:
            carry = 1
            value %= 10
        else:
            carry = 0
        return value

    current_lst = lst.head

    while current_1 is not None or current_2 is not None or carry > 0:
        digit = get_digit(current_1, current_2)
        lst.insert(digit)
        current_1 = current_1.get_next() if current_1 is not None else None
        current_2 = current_2.get_next() if current_2 is not None else None
    return lst


if __name__ == '__main__':
    lst1 = LinkedList()

    lst1.insert(4)
    lst1.insert(4)
    lst1.insert(3)
    print(list_to_num(lst1))

