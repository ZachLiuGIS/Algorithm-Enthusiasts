# two functions to calculate fibonacci

## fibonacci(n)

It uses a simple recursive function to calculate fibonacci number of n elements.

It is O(2^n) (less than that strictly because of less calls at the bottom).


## fibonacci_with_mem(n)

It uses memoization to cache the results and retrieve them if needed.

It is O(n).

When n = 35, fibonacci takes about 2692540 function calls while fibonacci_with_mem takes only about 123.
