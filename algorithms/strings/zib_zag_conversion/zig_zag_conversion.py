def zig_zag_conversion(str_, n_row):

    if n_row == 1:
        return str_

    length = len(str_)
    cycle = 2 * n_row - 2
    str_list = []

    i = 0
    while i < length:
        str_list.append(str_[i])
        i += cycle

    for i in range(1, n_row - 1):
        j = i
        while j < length:
            str_list.append(str_[j])
            second_index = j + cycle - i * 2
            if second_index < length:
                str_list.append(str_[second_index])
            j += cycle

    i = n_row - 1
    while i < length:
        str_list.append(str_[i])
        i += cycle

    return ''.join(str_list)