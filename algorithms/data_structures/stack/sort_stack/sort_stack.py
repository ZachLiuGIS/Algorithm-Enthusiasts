import sys

DATA_STRUCTURE_DIR = '../..'
sys.path.append(DATA_STRUCTURE_DIR)

from Stack import Stack


def sort_stack(stack):
    new_stack = Stack()
    temp_stack = Stack()

    while not stack.is_empty():
        if new_stack.is_empty():
            new_stack.push(stack.pop())

        else:
            data = stack.pop()
            while new_stack.peek() < data:
                temp_stack.push(new_stack.pop())
            new_stack.push(data)
            while not temp_stack.is_empty():
                new_stack.push(temp_stack.pop())
    return new_stack
