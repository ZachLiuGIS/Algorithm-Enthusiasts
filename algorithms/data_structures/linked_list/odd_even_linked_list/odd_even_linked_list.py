class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def odd_even_list(head):

    if not head or not (head and head.next):
        return head

    even_head = head.next
    odd_current = head
    even_current = even_head

    while even_current and even_current.next:
        odd_current.next = even_current.next
        even_current.next = even_current.next.next
        odd_current = odd_current.next
        even_current = even_current.next

    odd_current.next = even_head

    return head


if __name__ == '__main__':
    head = Node(1)
    current = head
    for i in range(2, 8):
        current.next = Node(i)
        current = current.next

    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    assert lst == [1, 2, 3, 4, 5, 6, 7]

    odd_even_list_head = odd_even_list(head)

    odd_even_lst = []
    current = odd_even_list_head
    while current:
        odd_even_lst.append(current.val)
        current = current.next
    assert odd_even_lst == [1, 3, 5, 7, 2, 4, 6]
