class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        # set push the old value to come after old header.
        new_node.next=self.head
        # set the new head as the new value
        self.head = new_node

    def delete(self, data ):
        current = self.head
        while current != None : 
            #remove first one
            if current.data == data :
                self.head  = current.next
            #remove other places
            elif current.next != None and current.next.data == data :
                current.next = current.next.next
            current = current.next

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def search(self, data):
        current = self.head
        while current != None:
            if current.data == data:
                print("found it")
                return current
            current = current.next
        return None


    def print(self):
        current = self.head
        while current != None:
            print(current.data,end="-")
            current = current.next
        print(" ")
        
#example of how to use it
# lk = LinkedList()
# lk.insert("a")
# lk.insert("b")
# lk.insert("c")
# lk.print()
# lk.search("a")
# lk.delete("c")
# lk.print()
# print(lk.size())

