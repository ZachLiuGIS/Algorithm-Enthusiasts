def length_of_longest_substring(s):
    """
    :type s: str
    :rtype: int
    """
    max_len = 0
    beginning = 0
    c_dict = {}

    for i, c in enumerate(s):
        if c in c_dict and c_dict[c] >= beginning:
            beginning = c_dict[c] + 1
        else:
            length = i - beginning + 1
            if length > max_len:
                max_len = length
        c_dict[c] = i

    return max_len


if __name__ == '__main__':
    assert length_of_longest_substring('') == 0
    assert length_of_longest_substring('aaaaaaa') == 1
    assert length_of_longest_substring('abcabcbb') == 3
    assert length_of_longest_substring('abcabcebb') == 4
    assert length_of_longest_substring('abcabcefg') == 6
