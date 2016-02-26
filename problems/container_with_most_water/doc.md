# Container with Most Water

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

## Brute Force

Iterate through the whole list and for each vertical line, test the current max area with the area formed between
the line and all lines after itself.
O(N2)

## Move from two sides

Start from the left most vertical line and the right most one.

If the left is shorter, the max area the left can be involved is from itself to the current right line.

Update the current max and move the current left one position left.

If the current right is shorter, do the inverse.

Keep track of max until current left and right meet each other.

O(N)