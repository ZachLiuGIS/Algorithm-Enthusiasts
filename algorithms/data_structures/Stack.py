class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class Stack:

    class Empty(Exception):
        pass

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def pop(self):
        if self.is_empty():
            raise self.Empty
        item = self.head.get_data()
        self.head = self.head.get_next()
        return item

    def peek(self):
        if self.is_empty():
            raise self.Empty
        return self.head.get_data()

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def print(self):
        lst = []
        current = self.head
        while current:
            lst.append(str(current.get_data()))
            current = current.get_next()
        print('->'.join(lst))
