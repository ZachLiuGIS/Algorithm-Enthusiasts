def is_isomorphic(s1, s2):

    if not len(s1) == len(s2):
        return False

    dict1 = {}
    dict2 = {}

    for i in range(len(s1)):
        if s1[i] not in dict1 and s2[i] not in dict2:
            dict1[s1[i]] = dict2[s2[i]] = i
        elif s1[i] in dict1 and s2[i] in dict2:
            if dict1[s1[i]] == dict2[s2[i]]:
                continue
            else:
                return False
        else:
            return False
    return True


if __name__ == '__main__':
    s1 = 'a'
    s2 = 'a'

    assert is_isomorphic(s1, s2) == True

    s1 = 'aa'
    s2 = 'ab'

    assert is_isomorphic(s1, s2) == False

    s1 = 'abdddfgg'
    s2 = 'cdeeelkk'

    assert is_isomorphic(s1, s2) == True