# One Step Away

this algorithm checks if one string is one edit away from another.

## One edit includes:
- insert a character
- remove a character
- replace a character

## Example
- pale, ple -> true
- pales, pale -> true
- pale, bale -> true
- pale, bake -> false

## Solution: find the one edit

if the length difference is greater than 1, return False

if the length are the same, walk through two strings together, and if different characters are at more than one 
locations, return False

if the length difference is 1, returns True if the longer character has one more character somewhere. So it can be
checked by walking through the two strings together. If there's a difference, jump to the next character for the longer
string. If there are any other differences, return False.