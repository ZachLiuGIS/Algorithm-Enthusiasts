import sys

DATA_STRUCTURE_DIR = '../..'
sys.path.append(DATA_STRUCTURE_DIR)

from Stack import Node, Stack


class StackWithMin(Stack):

    def __init__(self, *args, **kwargs):
        super(StackWithMin, self).__init__(*args, **kwargs)
        self.min_stack = Stack()

    def push(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

        try:
            min = self.min_stack.peek()
            if data <= min:
                self.min_stack.push(data)
        except Stack.Empty:
            self.min_stack.push(data)

    def pop(self):
        value = super(StackWithMin, self).pop()
        if value == self.min_stack.peek():
            self.min_stack.pop()
        return value

    def min(self):
        return self.min_stack.peek()
