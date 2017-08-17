def heap_sort(arr):
    def heapify(a):
        i = int(len(a) / 2) - 1
        while i >= 0:
            sink(arr, i, len(a) - 1)
            i -= 1

    def sink(a, i, n):
        while 2 * i <= n:
            j = 2 * i
            if j + 1 <= n and a[j] < a[j + 1]:
                j += 1
            if a[i] >= a[j]:
                break
            a[i], a[j] = a[j], a[i]
            i = j

    heapify(arr)
    end = len(arr) - 1

    while end > 0:
        arr[0], arr[end] = arr[end], arr[0]
        sink(arr, 0, end-1)
        end -= 1


if __name__ == '__main__':
    arr = [4, 7, 10, 2, 0, 5, -9, 13]
    heap_sort(arr)
    print(arr)
    assert arr == [-9, 0, 2, 4, 5, 7, 10, 13]
