# Write a function to find the longest common prefix string amongst an array of strings.

## Solution

the idea is to find the end index of common prefix. 

end index starts from 0, if all strings have the same character, move end index by 1. Otherwise we find 
the last index with common character.

> source: leetcode