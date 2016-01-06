# Insertion Sort

Iterate through the list, starting from the second element.

For each element, compare it with the elements in the left one by one until it finds one that is smaller than the
element. Move all elements larger than itself right one position, and then insert itself to the left of these
elements moved.

Repeat this until the last element.

The time is O(N^2) and space is O(1)