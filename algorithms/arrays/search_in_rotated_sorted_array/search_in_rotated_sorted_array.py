def search_in_rotated_sorted_array(nums, target):
    def binary_search(start, end):
        while start <= end:
            mid = (end + start) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    i = 0
    len_n = len(nums)
    if len_n == 1:
        return 0 if nums[0] == target else -1

    while i < len_n - 1 and nums[i] < nums[i + 1]:
        i += 1
    if i == len_n - 1:
        return binary_search(0, len_n - 1)
    elif target > nums[0]:
        return binary_search(0, i)
    elif target < nums[0]:
        return binary_search(i + 1, len_n - 1)
    else:
        return 0


if __name__ == '__main__':
    print(search_in_rotated_sorted_array([1, 3], 3))
