def is_strobogrammatic(num):
    """
    :type num: str
    :rtype: bool
    """
    maps = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}
    i = 0
    j = len(num) - 1
    while i <= j:
        if (num[i], num[j]) not in maps:
            return False
        i += 1
        j -= 1
    return True


def find_strobogrammatic(n):
    if n == 0:
        return [""]
    if n == 1:
        return ["0", "1", "8"]
    prev = []
    if n % 2 == 0:
        k = 0
    else:
        k = 1
    while k <= n:
        if k == 0:
            prev.append("")
        elif k == 1:
            prev.extend(["0", "1", "8"])
        else:
            if k == n:
                result = []
                for item in prev:
                    result.append("1" + item + "1")
                    result.append("8" + item + "8")
                    result.append("6" + item + "9")
                    result.append("9" + item + "6")
                return result
            else:
                new = []
                for item in prev:
                    new.append("0" + item + "0")
                    new.append("1" + item + "1")
                    new.append("8" + item + "8")
                    new.append("6" + item + "9")
                    new.append("9" + item + "6")
                prev = new
        k += 2


def strobogrammatic_in_range(low, high):
    maps = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}

    min_l, max_l = len(low), len(high)
    if min_l > max_l or (min_l == max_l and low > high):
        return 0

    ans = ["", "0", "1", "8"]
    count = 0
    while ans:
        tmp = []
        for w in ans:
            if len(w) < max_l or (len(w) == max_l and w <= high):
                if len(w) > min_l or (len(w) == min_l and w >= low):
                    if len(w) > 1 and w[0] == "0":
                        pass
                    else:
                        count += 1

                if max_l - len(w) >= 2:
                    for item in maps:
                        res = item[0] + w + item[1]
                        tmp.append(res)
        ans = tmp
    return count


if __name__ == '__main__':
    assert is_strobogrammatic('0') == True
    assert is_strobogrammatic('3') == False
    assert is_strobogrammatic('10') == False
    assert is_strobogrammatic('69') == True
    assert is_strobogrammatic('33') == False
    assert is_strobogrammatic('818') == True

    print(find_strobogrammatic(1))
    print(find_strobogrammatic(2))
    assert set(find_strobogrammatic(1)) == {'0', '1', '8'}
    assert set(find_strobogrammatic(2)) == {'11', '69', '88', '96'}

    print(strobogrammatic_in_range("0", "0"))
    print(strobogrammatic_in_range("50", "100"))
    assert strobogrammatic_in_range("0", "0") == 1
    assert strobogrammatic_in_range("50", "100") == 3
