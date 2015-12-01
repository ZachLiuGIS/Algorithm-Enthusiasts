import sys

DATA_STRUCTURE_DIR = '../..'
sys.path.append(DATA_STRUCTURE_DIR)

from Stack import Node, Stack


class StackQueue(object):

    class Empty(Exception):
        pass

    def __init__(self):
        self.main_stack = Stack()
        self.temp_stack = Stack()

    def enqueue(self, data):
        while not self.main_stack.is_empty():
            self.temp_stack.push(self.main_stack.pop())
        self.main_stack.push(data)
        while not self.temp_stack.is_empty():
            self.main_stack.push(self.temp_stack.pop())

    def dequeue(self):
        if self.is_empty():
            raise self.Empty
        return self.main_stack.pop()

    def is_empty(self):
        return self.main_stack.is_empty()

    def peek(self):
        if self.is_empty():
            raise self.Empty
        return self.main_stack.peek()
