def is_unique_characters_brute_force(str_):

    for i, c in enumerate(str_):
        if c in str_[i+1:]:
            return False
    return True


def is_unique_characters_by_sort(str_):

    str_sorted = ''.join(sorted(str_))

    for i in range(len(str_sorted) - 1):
        if str_sorted[i] == str_sorted[i+1]:
            return False
    return True


def is_unique_characters(str_):
    flags = [0] * 128

    for c in str_:
        if flags[ord(c)] == 1:
            return False
        else:
            flags[ord(c)] = 1
    return True

if __name__ == '__main__':
    print(is_unique_characters_brute_force('abcdefg'))
    print(is_unique_characters_brute_force('abcdefga'))
    print(is_unique_characters_by_sort('abcdefg'))
    print(is_unique_characters_by_sort('abcdefga'))
    print(is_unique_characters('abcdefg'))
    print(is_unique_characters('abcdefga'))
