# Check Permutation of Palindrome

the purpose is to check if an input string is a permutation of palindrome (a string which is the same forward or backward)

## count number of characters

A string is a permutation of palindrome if at most one character has odd occurrence. So the implementation store
the character count in a dictionary and then check that condition afterwards.

O(N)

## Other considerations

brute force of permutation is infeasible because of O(N!)

sorting and use a flag to test odd number occurrence is feasible but it is O(N * logN)
