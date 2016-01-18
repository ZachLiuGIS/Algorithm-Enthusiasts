def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return x

    flag = 1 if x >= 0 else -1
    num = abs(x)
    rev = 0
    count = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
        count += 1
    return rev * flag


def reverse_str(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return 0
    flag = 1 if x >= 0 else -1
    rev = int(''.join([c for c in str(abs(x))[::-1]])) * flag
    return rev if abs(rev) < 2 ** 31 else 0


if __name__ == '__main__':
    print(reverse(-123))
    print(reverse_str(-123))
