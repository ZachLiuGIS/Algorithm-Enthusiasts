## Sudoku puzzle

Determine if a Sudoku is valid, according to: [Sudoku Puzzles - The Rules](http://sudoku.com.au/TheRules.aspx).

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

![example](sudoku_example.png)

A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

## Solution
use three data structure to store visited characters in each row, col, and window.

if redundant character is found, it is invalid.

O(n)

> source: leetcode