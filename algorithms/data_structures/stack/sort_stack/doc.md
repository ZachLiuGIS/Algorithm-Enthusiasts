# Sort Stack

The purpose of the algorithm is to return a sorted stack with the smallest on top

An additional stack is used in the implementation

The algorithm creates a new stack, for each item popped from the input stack, items smaller will be pushed into
a temporary stack. After the popped data is pushed to the new stack, we added back items from the temporary stack 
one by one. So the new stack will remain sorted order with each push.

After all items are popped from input stack and pushed into new stack, the new stack contains all items from the input
in sorted order, which can be returned.

> source: Crack the Code Interview