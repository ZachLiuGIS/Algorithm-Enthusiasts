# Two Sum

Given an array of integers, find two numbers such that they add up to a specific target number.

If found, returns the first and second indices.

Index is 1 based.

## Brute force

For each item in array, check if there's another item in the rest of array can sum up to the target, return the two
indices if yes. Return None if not found.

O(N^2)

## Hash Table

Use a hash table (dict) to store the items when iterating, and for each item, check if the item that help sum up to the
target has been stored in the table.

If yes, then return the indices.

If no, return None.

O(N)


> source: Career Cup