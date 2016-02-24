## Strobogrammatic Number

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

For example, the numbers "69", "88", and "818" are all strobogrammatic.

### Write a function to determine if a number is strobogrammatic. The number is represented as a string.

The solution uses two pointers, one from beginning, one from the end.

Compare each pair, and then move lower pointer forward one position, and upper pointer backward one position.

To be strobogrammatic number, each pair has to be in the set

`{("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}`

So once a pair is not in the set, it is not strobogrammatic and thus return False

If no violation is found after the pointers cross each other, the whole string is strobogrammatic and return True.

### Find all strobogrammatic numbers that are of length = n

The solution interactively builds strobogrammatic number set from length 0 or 1, depending on odd or even length.

For each iteration, the result adds all possible pairs of characters on previous character set.

If the character length of for the set if n, the set is the final solution.

### Find the number of strobogrammatic numbers within a range

The solution will generate all strobogrammatic numbers from lower bound length, and check if each one is within range.

The count is added by 1 if True.

Then generate the next set of strobogrammatic numbers with two more characters, and
check each again.

The counting stops when the set of straobogrammatic numbers will contain numbers longer than upper bound length.