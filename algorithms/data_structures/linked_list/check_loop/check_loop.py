def check_loop(lst):
    node_set = set()
    current = lst.head
    while current:
        if current in node_set:
            return True
        node_set.add(current)
        current = current.get_next()
    return False
