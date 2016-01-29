# Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

## Solution

The solution uses two dictionaries to keep track of character pairs during iteration.

If neither character has appeared, a new pair will be stored. The character will be respective keys and same index be
stored as values.

If the character pair have both appeared in their respective dictionaries, check if they have the same value, which 
means the pair is legal(same character pair appeared at the same position before) and move to the next iteration. 

If the values(indices) are different, the two characters are mapped at different positions, and thus the string
is not isomorphic.

Similarly, if one character has been stored and the other not, the string is not isomorphic.

>source: leetcode