# Shell Sort

Shellsort is similar to insertion sort, but works a little faster by exchanging items that is further away instead of
next to each other. In this way, smaller ones are moved to the front more quickly.

1, at the beginning, the algorithm finds an appropriate h-value and then sorts the h sequence.

e.g. If there's an array a of length 10 and h is 4, the four sequence that are sorted are
- a[0], a[4], a[8]
- a[1], a[5], a[9]
- a[2], a[6], a[10]
- a[3], a[7]

2, after the array is h-sorted as explained above, h-value is shrink to smaller values and the fewer h sequences will be
sorted again.

3, keep doing 2 until h is 1 and the single sequence is sorted, which is the whole array.

the time is O(N^2) and the space is O(1)