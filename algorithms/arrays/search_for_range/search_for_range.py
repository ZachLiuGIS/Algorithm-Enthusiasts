def search_for_range(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    start = 0
    end = len(nums) - 1
    idx = 0
    if len(nums) == 0:
        return [-1, -1]
    if len(nums) == 1:
        return [0, 0] if nums[0] == target else [-1, -1]

    while start <= end:
        mid = (start + end) // 2
        if target > nums[mid]:
            start = mid + 1
        elif target < nums[mid]:
            end = mid - 1
        else:
            idx = mid
            break  # don't forget this

    if start > end:
        return [-1, -1]
    else:
        i_start = idx
        i_end = idx
        while i_start >= 0 and nums[i_start] == target:
            i_start -= 1
        while i_end < len(nums) and nums[i_end] == target:
            i_end += 1
        return [i_start + 1, i_end - 1]

if __name__ == '__main__':
    print(search_for_range([2, 2], 2))
