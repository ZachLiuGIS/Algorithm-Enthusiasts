## Depth First Search

Depth search starts from the root and searches through a path as long as it continues, and moves to the next
unvisited path when the previous one goes to end.

It can be implemented either through recursion or interactively through a stack.

## Breadth First Search

Breadth first search also starts from the root, but searches through all possible paths from the start at the same time.
At each round, the algorithm searches all possible vertices down one path. It goes on until all vertices are searched.

The best way to implemented breadth first search is through a queue. During one level of search, all vertices that need
to be search in the next level will be put in the queue. It stops when the queue becomes empty.
