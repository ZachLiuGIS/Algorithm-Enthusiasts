# Given an integer n, return the number of trailing zeroes in n!

## Solution

If there's a number that ends with 5 within n, there will be a 0. 

However, if the number is 25 (5 * 5), there will be two 0s.

So the count equals number of 5s + number of 5^2s, etc, given that all these numbers are within n.

>source: leetcode