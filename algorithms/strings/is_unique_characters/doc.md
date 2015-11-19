# Test if a string is composed of unique characters

## is_unique_characters_brute_force

This is brute force solution.

It compares each character in the string with all others, return false if and duplicates found, return true if no duplicates 
found for all characters.

O(N^2)

## is_unique_characters_by_sort

This solution sorts the string first, then only neighbors need to be compared to see if there are duplicates.

O(N * logN), sort is the bottleneck 

## is_unique_characters

This is the solution based on the book. It uses an array as flags. If a character is found in the string for the first 
time, the flag for that character is marked, so the second time, the string can be rejected.

O(N)