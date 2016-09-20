def longest_palindrome(s):
    if len(s) == 1:
        return s

    max_len = 1
    min_i, max_i = 0, 0

    for i in range(len(s)):
        j = k = i
        while j - 1 >= 0 and k + 1 < len(s) and s[j-1] == s[k+1]:
            j -= 1
            k += 1
        if k - j + 1 > max_len:
            max_len = k - j + 1
            min_i, max_i = j, k

    for i in range(len(s) - 1):
        j = i
        k = i + 1
        if not s[j] == s[k]:
            continue

        while j - 1 >= 0 and k + 1 < len(s) and s[j-1] == s[k+1]:
            j -= 1
            k += 1
        if k - j + 1 > max_len:
            max_len = k - j + 1
            min_i, max_i = j, k

    return s[min_i: max_i + 1]


def longest_palindrome_dp(s):
    """
    :type s: str
    :rtype: str
    """
    max_len = 1
    min_i, max_i = 0, 0
    length = len(s)
    lst = [[0] * length for i in range(length)]
    for i in range(length):
        lst[i][i] = 1
    for i in range(length - 1):
        if s[i] == s[i+1]:
            lst[i][i+1] = 2
            min_i, max_i = i, i + 1
        else:
            lst[i][i+1] = 1

    for i in range(length - 2):
        span = i + 2
        for j in range(length - span):
            if s[j] == s[j + span] and lst[j + 1][j + span - 1] == span - 1:
                lst[j][j + span] = span + 1
                if lst[j][j + span] > max_len:
                    max_len = lst[j][j + span]
                    min_i, max_i = j, j + span
            else:
                lst[j][j + span] = max(lst[j][j + span - 1], lst[j + 1][j + span])
    return s[min_i:max_i + 1]


if __name__ == '__main__':
    assert longest_palindrome('a') == 'a'
    assert longest_palindrome('abcabcee') == 'ee'
    assert longest_palindrome('abcdefgfedcba') == 'abcdefgfedcba'
    assert longest_palindrome('abcdefgfedcbaeeeee') == 'abcdefgfedcba'
    assert longest_palindrome('eeeeeabcdefgfedcba') == 'abcdefgfedcba'

    assert longest_palindrome_dp('a') == 'a'
    assert longest_palindrome_dp('ccc') == 'ccc'
    assert longest_palindrome_dp('abcabcee') == 'ee'
    assert longest_palindrome_dp('abcdefgfedcba') == 'abcdefgfedcba'
    assert longest_palindrome_dp('abcdefgfedcbaeeeee') == 'abcdefgfedcba'
    assert longest_palindrome_dp('eeeeeabcdefgfedcba') == 'abcdefgfedcba'
