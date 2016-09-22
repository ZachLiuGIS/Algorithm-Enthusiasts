def generate_parentheses(n):
    result = None
    for i in range(n):
        if i == 0:
            result = ["()"]
        else:
            prev_result = result[:]
            result = []
            for item in prev_result:
                for j in range(len(item) + 1):
                    str_ = '(' + item[:j] + ')' + item[j:]
                    if str_ not in result:
                        result.append(str_)
    return result


def generate_parentheses_dfs(n):
    def dfs(n, result, path, left, right):
        # check if the current path is valid
        if not is_valid(left, right, n):
            return
        # check we are at the right length
        if len(path) == n * 2:
            result.append(path)
            return
        dfs(n, result, path + '(', left + 1, right)
        dfs(n, result, path + ')', left, right + 1)

    def is_valid(left, right, n):
        # left paren <= right paren
        # left paren <= n
        # right paren >= n
        return right <= left <= n

    result = []
    dfs(n, result, '', 0, 0)
    return result


def generate_parentheses_3(n):
    def generate(p, left, right, parens=[]):
        if left:
            generate(p + '(', left - 1, right)
        if right > left:
            generate(p + ')', left, right - 1)
        if not right:
            parens += p,
        return parens

    return generate('', n, n)


print(generate_parentheses(3))
print(generate_parentheses_dfs(3))
print(generate_parentheses_3(3))
