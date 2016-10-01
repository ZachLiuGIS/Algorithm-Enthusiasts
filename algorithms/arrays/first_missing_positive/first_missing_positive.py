def first_missing_positive(nums):
    nums.append(0)
    l = len(nums)
    for i in range(l):
        if nums[i] < 0 or nums[i] >= l:
            nums[i] = 0
    for i in range(l):
        nums[nums[i] % l] += l
    for i in range(l):
        if nums[i] / l == 0:
            return i
    return l


def first_missing_positive_2p(nums):
    end = len(nums)
    if end == 0:
        return 1
    i = 0

    while i < end:
        if i == nums[i] - 1:
            i += 1
        elif nums[i] < 1 or nums[i] > end or nums[nums[i] - 1] == nums[i]:
            nums[i] = nums[end-1]
            end -= 1
        else:
            nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
    return i + 1

if __name__ == '__main__':
    assert(first_missing_positive([]) == 1)
    assert(first_missing_positive([1, 2, 0]) == 3)
    assert(first_missing_positive([3, 4, -1, 1]) == 2)
