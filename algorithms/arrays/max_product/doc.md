# Max Product of Sub Array

Find the max product of sub-array from an array of integers (positive or negative)

## Track max and min along the way

iterate the array, and keep track of max product

because items can be positive or negative or 0, need to track max and min along the way

max_ending and min_ending are used to track max and min products of current sub-array, 
while max_product tracks global max

when min_ending is negative, it may update max_ending if the next item is negative

if an item is 0, the max_ending will be 0 and restart updating, but max_product will have the global max, which will be returned 
at the end



time: O(N)
space: O(1)

