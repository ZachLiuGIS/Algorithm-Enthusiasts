# Bubble Sort

One of simplest sorting algorithm

During the first iteration, it compares each element to the next one, and swaps the two if the first one is larger. 
Therefore after the first iteration, the largest element will at the end.

During the second iteration, ignore the last element since it is already the largest. Compare each element as in the
previous iteration, and thus the second largest will be moved to the second last position.

Repeat the process until only the first two elements are compared and swapped if necessary. 

Then the sort will complete.

It is O(N^2) in time and O(1) in space.