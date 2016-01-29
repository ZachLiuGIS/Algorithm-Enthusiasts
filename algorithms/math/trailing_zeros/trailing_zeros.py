def trailing_zeros(n):
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count


if __name__ == '__main__':
    print(trailing_zeros(5))
    print(trailing_zeros(10))
    print(trailing_zeros(24))
    print(trailing_zeros(25))
    print(trailing_zeros(100))
