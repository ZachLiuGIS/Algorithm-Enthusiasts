from random import shuffle


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # shuffle array to make it random
    shuffle(arr)
    less = []
    greater = []
    equal = []
    pivot = arr[0]

    for x in arr:
        if x < pivot:
            less.append(x)
        elif x > pivot:
            greater.append(x)
        else:
            equal.append(x)
    return quick_sort(less) + equal + quick_sort(greater)


if __name__ == '__main__':
    arr = [4, 7, 10, 2, 0, 5, -9, 13]
    print(quick_sort(arr))
    assert quick_sort(arr) == [-9, 0, 2, 4, 5, 7, 10, 13]
