# Implement a class which implements a queue using two stacks

Because stack is last in last out, we can implement the queue using a main stack and a temporary stack.

When enqueue a data item, we can push all current data items into a temporary stack, push the new data 
into main stack, and then add old items from the temporary stack one by one. In this way, the order of the 
data items added are always ensured.

> source: Crack the Code Interview