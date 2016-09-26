# Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

## Brute Force
the simplest solution is stop at each character and see if the substring of enough length is a combination of all words.

## check by word length
keep all words in a hash_table for comparison 

the solution move index by word length and keep track of past words of strings, if consecutive words have the same composition of hash_table,
it is a combination and start index is added. 

> source: leetcode