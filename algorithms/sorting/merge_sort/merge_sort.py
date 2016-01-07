def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = int(len(arr) / 2)
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

    i = 0
    j = 0
    k = 0

    new_arr = []

    while k < len(left) + len(right):
        if i >= len(left):
            new_arr.append(right[j])
            j += 1
        elif j >= len(right):
            new_arr.append(left[i])
            i += 1
        elif left[i] < right[j]:
            new_arr.append(left[i])
            i += 1
        else:
            new_arr.append(right[j])
            j += 1
        k += 1

    return new_arr


if __name__ == '__main__':
    arr = [4, 7, 10, 2, 0, 5, -9, 13]
    print(merge_sort(arr))
    assert merge_sort(arr) == [-9, 0, 2, 4, 5, 7, 10, 13]
