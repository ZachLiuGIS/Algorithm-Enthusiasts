def remove_duplicates(lst):
    unique = set()
    current = lst.head
    while current:
        if current.get_data() not in unique:
            unique.add(current.get_data())
        else:
            lst.delete(current.get_data())
        current = current.get_next()
    return lst
