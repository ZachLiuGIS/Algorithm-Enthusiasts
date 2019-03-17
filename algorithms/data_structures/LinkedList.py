ss Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.next=self.head
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                print("found it")
                return current
            else:
                current = current.next
        return None

    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next=current.next
                return current
            prev = current
            current = current.next
        return None

    def print(self):
        current = self.head
        while current != None:
            print(current.data,end="-")
            current = current.next
        print(" ")
        

# Example of how to use it
# lk = LinkedList()
# lk.insert("a")
# lk.insert("b")
# lk.insert("c")
# lk.print()
# lk.search("d")
# lk.delete("c")
# lk.print()

