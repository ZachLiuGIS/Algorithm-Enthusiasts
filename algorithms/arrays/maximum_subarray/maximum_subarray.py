import sys


def maximum_subarray_dp(nums):
    # need fix
    len_n = len(nums)
    dp = [[0] * len_n for i in range(len_n)]
    for i in range(len_n):
        dp[i][i] = nums[i]
    for i in range(1, len_n):
        for j in range(len_n - i):
            dp[j][j + i] = max(dp[j][j + i - 1] + nums[j + i], dp[j + 1][j + i])
    return dp[0][len_n - 1]


def maximum_subarray(nums):
    max_sum = nums[0]
    l, r, total = 0, 0, 0
    while r < len(nums):
        total += nums[r]
        if total > max_sum:
            max_sum = total
        if total <= 0:
            l, r = r + 1, r + 1
            total = 0
        else:
            r += 1
    return max_sum


if __name__ == '__main__':
    print(maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
