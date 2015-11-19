def str_permutation(str_):
    permutations = []

    def get_permutation(s, prefix):
        if len(s) == 0:
            permutations.append(prefix)
        else:
            for i, c in enumerate(s):
                get_permutation(s[:i] + s[i+1:], prefix + c)

    get_permutation(str_, '')

    return permutations


def check_permutation_brute_force(str1, str2):
    if not len(str1) == len(str2):
        return False

    permutations = str_permutation(str1)
    return str2 in permutations


def check_permutation_sort(str1, str2):
    if not len(str1) == len(str2):
        return False

    new_str1 = ''.join(sorted(str1))
    new_str2 = ''.join(sorted(str2))
    return new_str1 == new_str2


def check_permutation_find_replace(str1, str2):
    if not len(str1) == len(str2):
        return False

    str_list = [c for c in str1]

    for c in str2:
        try:
            i = str_list.index(c)
            str_list[i] = None
        except ValueError:
            return False
    return True


def check_permutation_count_chars(str1, str2):
    if not len(str1) == len(str2):
        return False

    char_count = {}

    for c in str1:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    for c in str2:
        if c in char_count:
            char_count[c] -= 1
            if char_count[c] < 0:
                return False
        else:
            return False

    return True


if __name__ == '__main__':
    print(check_permutation_brute_force('abcdef', 'dcbfea'))
    print(check_permutation_brute_force('abcdef', 'dcaafe'))
    print(check_permutation_sort('abcdef', 'dcbfea'))
    print(check_permutation_sort('abcdef', 'dcaafe'))
    print(check_permutation_find_replace('abcdef', 'dcbfea'))
    print(check_permutation_find_replace('abcdef', 'dcaafe'))
    print(check_permutation_count_chars('abcdef', 'dcbfea'))
    print(check_permutation_count_chars('abcdef', 'dcaafe'))
