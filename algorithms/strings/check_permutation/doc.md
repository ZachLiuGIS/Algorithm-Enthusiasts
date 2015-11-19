# Check Permutation

given two strings, check if one is the permutation of the other

## brute force

get permutations of a string and compare the other with each. 

O(N!)

## sort and compare

sort the two strings, if the two strings are the same after sort, return True, return False otherwise.

O(N * logN)

## linear search and replace

search each character of one string in another string, return False if none is found. If it is found, replace it with
None and search the next character.

O(N^2)

## count char numbers

count char numbers of the first string and test if the char count of each character in the second string match.

O(N)