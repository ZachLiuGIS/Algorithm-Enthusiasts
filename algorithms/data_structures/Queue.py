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


class Queue:

    class Empty(Exception):
        pass

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            raise self.Empty
        value = self.head.get_data()
        self.head = self.head.get_next()
        if self.is_empty():
            self.tail = None
        return value

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
