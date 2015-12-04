def selection_sort(lst):
    length = len(lst)
    for i in range(length - 1):
        min_index = i
        for j in range(i, length):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst
