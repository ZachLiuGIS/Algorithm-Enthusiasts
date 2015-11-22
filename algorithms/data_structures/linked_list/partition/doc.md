# Partition a Linked List

The purpose of the algorithm is to partition a LinkedList by a value such that the all nodes with data smaller than
the partition value are in front of nodes above or equal to the partition value

e.g. input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
     output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
     
## Store nodes in two separate lists and combine after

Keep all nodes with data below the partition value in one LinkedList and others in another LinkedList

Then connect the first one with the second one to return the combined LinkedList

O(N)
