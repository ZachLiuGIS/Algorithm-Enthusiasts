# Rotate Matrix

## Rotate Matrix

This function implements a rotate function which also accept a degree of 90, 180, 270, etc.

It returns a new matrix, and assign each element from original matrix to their new position based on 
rotation formula.

O(N^2), and need O(N^2) extra space.

## Rotate Matrix in place

This function implements matrix rotation in place, so there's no new matrix created and the same matrix is returned

It rotate one ring at a time from outside.

For each ring, it rotates corresponding cells on the four sides in one iteration, and then goes to the next four
corresponding cells.

O(N^2), and need O(1) extra space.