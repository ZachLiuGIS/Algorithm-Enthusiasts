def get_char_count(str_):
    char_count = {}
    for c in str_:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count


def max_one_odd(count_dict):
    odd_count = 0
    for key in count_dict:
        if count_dict[key] % 2 == 1:
            odd_count += 1
            if odd_count > 1:
                return False
    return True


def check_permutation_of_palindrome(str_):
    char_count = get_char_count(str_)
    return max_one_odd(char_count)


if __name__ == '__main__':
    assert check_permutation_of_palindrome('abcab') == True
    assert check_permutation_of_palindrome('abcaa') == False
