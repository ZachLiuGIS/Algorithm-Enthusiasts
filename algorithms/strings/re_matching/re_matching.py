def is_match(s, p):
    i = 0
    j = 0
    while i < len(s) and j < len(p):
        if s[i] == p[j]:
            i += 1
            j += 1
            continue
        elif p[j] == '.':
            i += 1
            j += 1
            continue
        elif p[j] == '*':
            if j == len(p) - 1:
                return True
            while i < len(s) and s[i] != p[j+1]:
                i += 1
            j += 1
    if i == len(s):
        return True
    else:
        return False


def is_match_dp(s, p):
    len_s, len_p = len(s), len(p)
    dp = [[False] * (len_p + 1) for i in range(len_s + 1)]

    dp[0][0] = True
    for j in range(2, len_p + 1): 
        dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'

    for i in range(1, len_s + 1):
        for j in range(1, len_p + 1):
            dp[i][j] = dp[i][j - 2] or (p[j - 2] in (s[i - 1], '.') and dp[i - 1][j]) if p[j - 1] == '*' \
                else dp[i - 1][j - 1] and p[j - 1] in ('.', s[i - 1])
    return dp[len_s][len_p]


if __name__ == '__main__':
    assert is_match_dp('aa', 'aa') == True
    assert is_match_dp('aa', 'a') == False
    assert is_match_dp('aa', '*') == False
    assert is_match_dp('aa', '.*') == True
    assert is_match_dp('ab', 'a*b') == True
    assert is_match_dp('aab', 'aa*b'), True
    assert is_match_dp('aab', 'c*a*b'), True
