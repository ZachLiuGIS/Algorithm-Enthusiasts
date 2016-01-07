# Merge Sort

merge sort is a divide and conquer algorithm, then underlying concept is to merge two smaller ordered sequence into a 
larger one. 

It will keep divide the whole list into sub list until sub lists are single items, and all single items are sorted.

Then these recursive calls will be merged until we have one whole sorted list at the end.

the time is O(N*LogN) and the space is O(N)