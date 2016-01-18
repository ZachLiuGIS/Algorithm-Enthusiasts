# Length of Longest Substring

Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
For "bbbbb" the longest substring is "b", with the length of 1.

The solution uses a dict to keep track of visited characters and a int to track 
current beginning index of substring without repeating

> source: leetcode