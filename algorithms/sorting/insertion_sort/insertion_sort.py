def insertion_sort(lst):
    length = len(lst)
    for i in range(1, length):
        num = lst[i]
        j = i - 1

        while j >= 0:
            if lst[j] > num:
                lst[j+1] = lst[j]
                j -= 1
            else:
                break
        lst[j+1] = num
    return lst
