# Return Kth to Last

this algorithm finds the kth to last element of a singly linked list.

## get_kth_to_last

This function wraps a recursive function to put each recursive call on a stack, and move the head one node forward
toward the end.

It uses an index starts from 0 to track the calls backwards, and when the index == k, it is called kth times so the 
head should be the kth node. A nonlocal value is used to store the node and return later by the outer function.

If k is longer then the size of list, it will return None.



> source: cracking the code interview