def string_to_integer(str):
    i = 0
    flag = 1
    while i < len(str) and str[i] == " ":
        i += 1
    if i == len(str):
        return 0

    if str[i] == "+":
        i += 1
    elif str[i] == "-":
        i += 1
        flag = -1

    if i == len(str) or str[i] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        return 0

    start = i
    while i < len(str) and str[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        i += 1
    end = i

    if flag == 1:
        return min(int(str[start:end]), 2147483647)
    else:
        return max(-int(str[start:end]), -2147483648)


if __name__ == '__main__':
    assert string_to_integer('') == 0
    assert string_to_integer('+') == 0
    assert string_to_integer('+-2') == 0
    assert string_to_integer('+123') == 123
    assert string_to_integer('-123') == -123
    assert string_to_integer('  +22ab') == 22
    assert string_to_integer('    -13 ') == -13
    assert string_to_integer('abc') == 0
    assert string_to_integer('-abc') == 0
    assert string_to_integer('-2147483649') == -2147483648
    assert string_to_integer('+2147483647') == 2147483647
