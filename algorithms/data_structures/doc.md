# This is a directory for data_structures

## LinkedList
This implementation of LinkedList is singly which means each node only points to the next, not the previous.

The Node contains the value and reference of the next Node

The Node has the following public methods

- get_data(): return the data hold by the node
- get_next(): return the reference to the next Node
- set_next(node): set the reference to the next Node

The LinkedList has the following public methods

- size(): return the number of nodes
- insert(data): insert data at the head
- search(data): return True if a node has the data item
- delete(data): delete a node with the data, throw ValueError if data not found
- print(): print the whole LinkedList, throw ValueError if data not found


## Stack

Stack is implemented using a LinkedList

Stack has the following public methods

- size(): return the number of items(nodes) of the stack
- push(data): add a data item to the stack
- pop(): return and get rid of the last item added, throw Stack.Empty if empty
- peek(): return the data of the last item added without delete, throw Stack.Empty if empty
- is_empty(): return True if stack is empty
- print(): print the whole stack data

## Queue

Queue is also implemented using a LinkedList

Queue has the following public methods

- size(): return the number of items(nodes) of the queue
- enqueue(data): add a data item to the queue
- dequeue(): return the first data on the queue and get rid of the node, throw Queue.Empty if empty
- peek(): return the first data on the queue without delete, throw Queue.Empty if empty
- is_empty(): return True if queue is empty
- print(): print the whole queue data


## PriorityQueue (Max and Min)

Both Max and Min Priority Queues are implemented using an array, which represents the binary heap.

the first item of the internal array is always None and the max/min is stored at index 1.

MaxPQ and MinPQ have the following public methods

- size(): return the size of the pq
- is_empty(): return if the pq is empty
- insert(): insert a new item into the pq
- peek_min()/peek_max(): get the max item (MaxPQ) or min item(MinPQ) from the pq without delete
- del_min()/del_max(): delete and return the max item (MaxPQ) or min item(MinPQ) from the pq


## BinarySearchTree

A binary search tree is a binary tree where keys that are less than their parent are at the left subtree while those
larger are at the right subtree.

The BinarySearchTree class uses internal Node class to represent each tree node, and each node stores a key-value pair

The Binary Search Tree class has the following public methods

- size(): return the size of the tree
- get(key): get the value associated with the key
- put(key, value): update the value associated with the key if key exists, create a new node otherwise
- min(): get the min key of the tree
- max(): get the max key of the tree
- floor(key): get the largest key in the tree that is less than or equal to the given key
- select(rank): get the key that has rank number of keys smaller than itself
- rank(key): get the number of keys that are smaller than the given key
- delete_min(): delete the node with the smallest key
- delete(key): delete the node with the given key
- keys(lo, hi): get the keys within the (lo, hi) range


## LeftLeanRedBlackTree

This is a python implementation of left lean RedBlackTree implemented based on Sedgewick's Algorithms 4th edition

[reference](https://www.cs.princeton.edu/~rs/talks/LLRB/RedBlack.pdf)

[source](http://algs4.cs.princeton.edu/33balanced/RedBlackBST.java.html)

The Binary Search Tree class has the following public methods

- size(): return the size of the tree
- get(key): get the value associated with the key
- put(key, value): update the value associated with the key if key exists, create a new node otherwise
- min(): get the min key of the tree
- max(): get the max key of the tree
- delete_min(): delete the node with the smallest key
- delete_max(): delete the node with the smallest key
- delete(key): delete the node with the given key



