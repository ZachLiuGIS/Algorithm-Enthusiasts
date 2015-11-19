def binary_search(arr, value):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = int((lo + hi) / 2)
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            lo = mid + 1
        else:
            hi = mid - 1

    return False


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search(arr, 8))
    print(binary_search(arr, 9))
