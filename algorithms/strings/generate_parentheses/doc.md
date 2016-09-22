# Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

## Solution 1
This is a simple solution, that just builds strings from n = 1 to n = n. For each iteration, it adds a ( and a ) 
to all previous strings at all possible solutions. Duplicate ones should be dropped.

## Solution 2
This solution uses dfs, it builds from the first character until all n*2 characters are filled. Throughout the
paths, only valid strings are allowed.

generate_parentheses_3 is a simplified version.

>source: leetcode