def shell_sort(arr):
    length = len(arr)
    h = 1
    # find the starting h value
    while h < length / 3:
        h = 3 * h + 1

    while h >= 1:
        for i in range(h, length):
            tmp = arr[i]
            pos = i
            while pos >= h and arr[pos - h] > tmp:
                arr[pos] = arr[pos - h]
                pos -= h
            arr[pos] = tmp
        h = int(h / 3)
    return arr


if __name__ == '__main__':
    arr = [4, 7, 10, 2, 0, 5, -9, 13]
    print(shell_sort(arr))
    assert shell_sort(arr) == [-9, 0, 2, 4, 5, 7, 10, 13]
