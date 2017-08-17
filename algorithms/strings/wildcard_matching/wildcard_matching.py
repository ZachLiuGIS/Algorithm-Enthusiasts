def wildcard_matching_dp(s, p):
    len_s = len(s)
    len_p = len(p)
    dp = [[False] * (len_p + 1) for i in range(len_s + 1)]
    dp[0][0] = True
    for j in range(1, len_p + 1):
        dp[0][j] = p[j - 1] == "*" and dp[0][j - 1] == True
    for i in range(1, len_s + 1):
        for j in range(1, len_p + 1):
            if p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j - 1] and p[j - 1] == s[i - 1]
    return dp[len_s][len_p]


def wildcard_matching(s, p):
    i, j, x, y, l = 0, 0, 0, -1, len(p)
    while i < len(s):
        if j < l and (p[j] == '?' or p[j] == s[i]):
            i += 1
            j += 1
        elif j < l and p[j] == '*':
            x = i
            y = j
            j += 1
        elif y >= 0:
            x += 1
            i = x
            j = y + 1
        else:
            return False
    while j < l and p[j] == '*':
        j += 1
    return j == l


if __name__ == '__main__':
    assert (wildcard_matching("aaaaaaaaaaaaaaaaaaaaa", "*") == True)
    assert (wildcard_matching("abbaba", "a*a*a") == True)
    assert(wildcard_matching_dp("aaaaaaaaaaaaaaaaaaaaa", "*") == True)
    assert(wildcard_matching_dp("aaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa") == False)
    assert(wildcard_matching_dp("adfdfffffff", "ad?*") == True)
