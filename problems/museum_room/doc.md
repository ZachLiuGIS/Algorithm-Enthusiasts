## Museum Room Question

There is a museum organized as NxN room. Some rooms are locked and inaccessible.
Other rooms are open and some rooms have guards. Guards can only move north, south, east and west,
only through open rooms and only within the museum. For each room, find the shortest distance to a guard.
What is the time complexity of your algorithm?

## Analysis

The room can be modelled as a N * N matrix, with 0 = locked room, 1 = open room, 2 = room with a guard.

e.g.

```python
[
    [0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 2, 1, 0],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 1, 1, 0, 2],
    [2, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 1, 0]
]
```

One solution is to create a graph from the matrix, and use breadth first search to find the shortest paths to guards.