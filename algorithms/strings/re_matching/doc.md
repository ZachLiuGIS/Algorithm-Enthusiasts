# Regular Expression Matching

Implement regular expression matching with support for `.` and `*`.

## Dynamic Programming solution

The problem is complex at a glance, so dynamic programming comes to mind since it builds complex solution from
simpler partial solutions.

To begin with, build a matrix where m[i][j] (True/False) means if first j characters of pattern can match first i
characters of input string. Because empty strings need to be taken care of, the matrix is len(s) + 1 by len(p) + 1

To initialize the matrix, m[0][0] is always T because empty string matches empty string. And char+ '*' + char + '*'
can match empty string too. So if the pattern is c*c*c*ccc, first row of the matrix should be TFTFTFTFFF. All other
elements are False since we don't know if they match.

Then the dp process kicks in. For each m[i][j] to be true there are following scenarios:
    - if p[j - 1] (current pattern character) is '*':
        - m[i][j - 2] is T (* means 0 occurance of previous character)
        - m[i-1][j] is T and p[i-2] == s[i-1] or '.' (* can take the current string character in the set it represents)
    - if p[j - 1] is not '*':
        - m[i-1][j-1] is T and p[j - 1] == s[i - 1] (previours characters match,
        the current pattern char match the current string char)
        - m[i-1][j-1] is T and p[j - 1] == '.' (the same)

return True if m[len(s)][len(p)] is True. (the whole pattern matches the whole string)

> source: leetcode