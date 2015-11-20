from collections import OrderedDict


def simple_compression(str_):
    result = []
    letter = str_[0]
    count = 0

    for c in str_:
        if not c == letter:
            result.append(letter)
            result.append(str(count))
            letter = c
            count = 0
        count += 1

    result.append(letter)
    result.append(str(count))
    return ''.join(result)


if __name__ == '__main__':

    assert simple_compression('aabcccccaaa') == 'a2b1c5a3'
    assert simple_compression('eeeaaffffffkl') == 'e3a2f6k1l1'
    assert simple_compression('kklll****(nnnnnmm)') == 'k2l3*4(1n5m2)1'