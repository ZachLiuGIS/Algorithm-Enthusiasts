def longest_valid_parentheses_dp(s):
    """
    :type s: str
    :rtype: int
    """
    if s == "":
        return 0
    len_s = len(s)
    m = [[0] * len_s for i in range(len_s)]
    for i in range(len_s):
        m[i][i] = 0
    for i in range(len_s - 1):
        if s[i] == '(' and s[i + 1] == ')':
            m[i][i + 1] = 2
        else:
            m[i][i + 1] = 0
    for i in range(len_s - 2):
        k = 2 + i
        for j in range(0, len_s - k):
            m[j][j + k] = max(m[j][j + k - 1], m[j + 1][j + k])
            if s[j] == '(' and s[j + k] == ')' and m[j + 1][j + k - 1] == k - 1:
                m[j][j + k] = k + 1
            else:
                for n in range(j + 1, j + k - 1):
                    if m[j][n] + m[n + 1][j + k] == k + 1:
                        m[j][j + k] = k + 1
    return m[0][len_s - 1]


def longest_valid_parentheses_dp2(s):
    dp = [0] * len(s)
    max_ = 0
    for i in range(1, len(s)):
        if s[i] == ')':
            j = i - 1 - dp[i - 1]
            if j >= 0 and s[j] == '(':
                dp[i] = dp[i - 1] + 2
                if j - 1 >= 0:
                    dp[i] += dp[j - 1]
                max_ = max(max_, dp[i])
    return max_


def longest_valid_parentheses_stack(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(['(', i])
        elif s[i] == ')' and len(stack) == 0:
            stack.append([')', i])
        else:
            if stack[-1][0] == '(':  # valid matches '()' are removed from stack
                del stack[-1]
            else:
                stack.append([')', i])
    if len(stack) == 0:  # stack is empty when s is valid
        return len(s)

    invalid = [-1]  # start index
    for item in stack:
        invalid.append(item[1])  # the indexes of no-matched '(' or ')'
    invalid.append(len(s))  # end index
    res = 0
    for i in range(0, len(invalid) - 1):
        res = max(res, invalid[i + 1] - invalid[i] - 1)  # find the longest valid substring
    return res


if __name__ == '__main__':
    assert (longest_valid_parentheses_dp("(()())") == 6)
    assert (longest_valid_parentheses_dp("()(())") == 6)
    assert (longest_valid_parentheses_dp2("(()())") == 6)
    assert (longest_valid_parentheses_dp2("()(())") == 6)
    assert (longest_valid_parentheses_stack("(()())") == 6)
    assert (longest_valid_parentheses_stack("()(())") == 6)
