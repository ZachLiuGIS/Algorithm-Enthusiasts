import cProfile


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_with_mem(n):
    mem = []
    for j in range(n+1):
        mem.append(0)

    def get_fib(i):
        if i <= 0:
            return 0
        elif i == 1:
            return 1
        if mem[i] > 0:
            return mem[i]
        mem[i] = get_fib(i-1) + get_fib(i-2)
        return mem[i]

    for item in range(n):
        get_fib(item + 1)

    return mem[n]


if __name__ == '__main__':
    cProfile.run('fibonacci(30)')
    cProfile.run('fibonacci_with_mem(30)')
