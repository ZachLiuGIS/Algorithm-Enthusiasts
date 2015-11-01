# Problem Description

An island kingdom (represented by a matrix) has islands (1) and water (0). Here is an example

```
0 0 0 1 0
1 1 0 1 1
1 0 0 0 1
0 1 1 0 0
```

if 1 is connected with 1 from above, below, left, or right, they are counted as one island. So the example
above should have three islands.

The objective is to count how many islands there are in the kingdom, given the kingdom matrix.


# Solutions

Two solutions have been written

## Solution 1: 

using two loops, one to count horizontally, then use the other to reduce redundant counts.

## Solution 2:

use recursion to find the first piece of an island and then recursively find all other pieces of the same island
and count as 1, then on to the next island.