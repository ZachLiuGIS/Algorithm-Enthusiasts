# Simple Compression

It uses counts of repeated characters to compress a string.

E.g. 'eeeaaffffffkl' -> 'e3a2f6k1l1'

## count as walking throught the string

keep track of which letter it is counting and number of repeats. 

Once the letter changes, add the letter and count into result.

O(N)

