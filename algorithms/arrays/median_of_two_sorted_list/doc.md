# Median of two sorted list

here are two sorted arrays lst1 and lst2 of size m and n respectively. Find the median of the two sorted arrays.

## Merge Sort solution

Merge sort can be used to find the solution because lists are sorted. Keeps adding minimum from the two lists until it
reaches the median one or ones.

O(m+n)

## Divide and Conquer solution

This is a faster solution, the idea is to find the kth smallest. So if the two lists have n items, you only need to find
(n/2 + 1)th smallest if n is odd, or ((n/2)th + (n/2 +1)th) / 2 smallest if n is even.

It uses two pointers to track elements that have been excluded from the two lists, starting from 0. Then it uses
recursion to keep excluding about half of the elements that are smaller, until it reaches the kth element, which
is the median.
