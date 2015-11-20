def check_one_edit_away(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    elif len(str1) == len(str2):
        flag = 0
        for i in range(len(str1)):
            if not str1[i] == str2[i]:
                flag += 1
                if flag > 1:
                    return False
        return True

    elif len(str1) - len(str2) == 1:
        flag = 0
        i, j = 0, 0
        while i < len(str2):
            if not str1[i] == str2[j]:
                i += 1
                flag += 1
                if flag > 1:
                    return False
            else:
                i += 1
                j += 1
        return True

    else:
        flag = 0
        i, j = 0, 0
        while i < len(str1):
            if not str1[i] == str2[j]:
                j += 1
                flag += 1
                if flag > 1:
                    return False
            else:
                i += 1
                j += 1
        return True


if __name__ == '__main__':

    assert check_one_edit_away('pale', 'ple') == True
    assert check_one_edit_away('pales', 'pale') == True
    assert check_one_edit_away('pale', 'bale') == True
    assert check_one_edit_away('pale', 'bake') == False

