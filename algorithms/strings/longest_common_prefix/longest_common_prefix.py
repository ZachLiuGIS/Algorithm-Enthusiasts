def longest_common_prefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return ""
    end = 0
    while True:
        flag = True
        ch = None
        for i, str_ in enumerate(strs):
            if end == len(str_):
                flag = False
                break
            if i == 0:
                ch = str_[end]
            else:
                if not str_[end] == ch:
                    flag = False
                    break
        if not flag:
            break
        end += 1
    return strs[0][:end]


def longest_common_prefix_2(strs):
    if not strs:
        return ''
    str_ = ''
    min_len = min([len(s) for s in strs])
    for i in range(min_len):
        char = strs[0][i]
        if any(s[i] != char for s in strs):
            break
        str_ += char
    return str_


if __name__ == '__main__':
    assert longest_common_prefix(['']) == ''
    assert longest_common_prefix(['a']) == 'a'
    assert longest_common_prefix(['ab', 'abc']) == 'ab'
    assert longest_common_prefix(['ab', 'abcd', 'abbbb']) == 'ab'
