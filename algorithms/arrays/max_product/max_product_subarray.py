def get_max_product_subarray(arr):
    max_ending = arr[0]
    min_ending = arr[0]
    max_product = arr[0]

    for item in arr[1:]:
        max_ending = max(max(max_ending * item, min_ending * item), item)
        min_ending = min(min(max_ending * item, min_ending * item), item)
        max_product = max(max_ending, max_product)
    return max_product


if __name__ == '__main__':
    arr1 = [1, 4, 0, 5, 3]
    assert get_max_product_subarray(arr1) == 15

    arr2 = [1, 4, 0, -5, 3]
    assert get_max_product_subarray(arr2) == 4

    arr3 = [1, -4, 0, -5, 3]
    assert get_max_product_subarray(arr3) == 3

    arr4 = [1, -4, 0, -5, -3]
    assert get_max_product_subarray(arr4) == 15

    arr5 = [1, -4, 0, -5, 0]
    assert get_max_product_subarray(arr5) == 1

    arr6 = [-4, 0, -5]
    assert get_max_product_subarray(arr6) == 0
