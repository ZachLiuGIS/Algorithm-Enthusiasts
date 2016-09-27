def next_permutation(nums):
    def find_min_larger_index(idx, n):
        while idx < len(nums) and nums[idx] > n:
            idx += 1
        return idx - 1

    i = len(nums) - 1
    while i > 0 and nums[i] <= nums[i-1]:
        i -= 1
    if i == 0:
        nums.reverse()
    else:
        idx = find_min_larger_index(i, nums[i-1])
        nums[idx], nums[i-1] = nums[i-1], nums[idx]
        start = i
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

if __name__ == '__main__':
    nums = [5, 1, 1]
    next_permutation(nums)
    assert(nums == [1, 1, 5])

    nums = [2, 1, 4, 3]
    next_permutation(nums)
    assert(nums == [2, 3, 1, 4])

    nums = [1, 5, 1]
    next_permutation(nums)
    assert(nums == [5, 1, 1])
