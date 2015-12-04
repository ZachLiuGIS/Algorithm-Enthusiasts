# Zig Zag Conversion

Given a string in zigzag pattern based on a number of rows, return a string read line by line

e.g:

input string: PAYPALISHIRING in 3 rows

P A H N
APLSIIG
Y I R

output string: PAHNAPLSIIGYIR

## solution: divide string in cycles and read characters line by line

The indices of the input string is like

0   4   8     12
1 3 5 7 9  11 13
2   6   10

Based on observation, the zigzag pattern repeat in cycles, each cycle contains n + n - 2 = 2n - 2 elements

The first row has indices 0, 0 + cycle, 0 + cycle * 2, etc

The last row has indices n-1, n-1 + cycle, n-1 + cycle * 2, etc

For lines in the middle, there are two elements. 
It goes like this: i, i + cycle - 2i, i + cycle, i + cycle + cycle - 2i, etc

For each row, the adding ends when index is outside of length of input string.

The whole solution is to process line from 0 to n-1 and the characters should be in the correct returned order, which is
0, 4, 8, 12, 1, 3, 5, 7, 9, 11, 13, 2, 6, 10

> source: Career Cup