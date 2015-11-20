# A collection of traps in python

## use multiplication to create two dimensional list

```
matrix = [[0] * length] * length
print(matrix)

[[0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]]
 
 
matrix[0][0] = 1
print(matrix)

[[1, 0, 0, 0, 0],
 [1, 0, 0, 0, 0],
 [1, 0, 0, 0, 0],
 [1, 0, 0, 0, 0],
 [1, 0, 0, 0, 0]]
```

this will reused the same list multiple times and cause bugs


 
