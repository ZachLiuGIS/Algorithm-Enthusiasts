# First Missing Positive

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

## Solution 1

the range of missing value should be 1 to len(nums) + 1

so first making all those 0. because there may not be 0, so we append 0 at the end to start.

the main idea is to add a value to the corresponding array position if a value is not missed. We can use
nums[nums[i] % len(nums)] += len(nums) to do that. e.g. If 3 is missing, nums[3] should be 0, otherwise, it will be 3.

At the end, we find the first position with value 0, which means the number of the position is missing.

## Solution 2

The solution starts from position 0. If position is 1 less than its number (since index is 0 based), we have the
corresponding number not missing, so we move to the next. (1 should be at position 0)

If current number is not that number, we exclude too small and too large numbers, or the current number is already
in it position. e.g. current position 0 is 3, but there's a 3 at position 2. In these cases, we move the current number
to the end of array and discard that position since that is useless.

If the number at current position can be moved to its correct position (e.g. current position 1 has number 3,
but position 2 is not 3), we swap it with the value at that position.

at the end the iteration will stop when all candidate numbers are at position and useless numbers are discarded. So
the current index + 1 should be the missing value


> source: leetcode