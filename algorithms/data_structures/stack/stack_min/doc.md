# Implement a Stack that tracks the min of the stack

push(), pop() and min() should all be O(1)

## Extend Stack with an extra stack to track the min

when push an item into the stack, if the data is equal to or smaller than the current min in the stack,
push the value into the current min stack. Pushing values that are equal to current min is because 
they can be safely popped when the value is popped in the main stack.

> source: Crack the Code Interview

