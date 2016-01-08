# Heap Sort

Heap sort uses a binary heap to continuously provide the min item until the whole list is sorted. The algorithm two 
phases to sort a list in place and thus avoiding extra space.

## Phase 1: construct a heap in place

The process start from the bottom to make small sub heaps.

Then sinking the parent of two sub heaps will provide a larger sub heap.

Do this until the whole list is in heap order.

Because each end item is itself a heap, we can start from half way of the list and construct up until the root.

## Phase 2: sort the heap continues 

1, Exchange the root and the last item in the list, the largest item will sit at the end of the list.

2, Take the list excluding the last and sink the root, will restore heap order, then exchange the root and the second last
item and the second last will be the second largest.

3, Repeat the process and at the end the whole list will be in sorted order.

## the time is O(N*LogN) and the space is O(1)
