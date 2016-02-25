import cProfile


def median_of_two_sorted_list1(lst1, lst2):
    len1 = len(lst1)
    len2 = len(lst2)
    i = 0
    j = 0
    k = (len1 + len2) // 2
    cnt = 0
    lst = []
    while not (i == len1 and j == len2):
        if i == len1:
            lst.append(lst2[j])
            j += 1
        elif j == len2:
            lst.append(lst1[i])
            i += 1
        elif lst1[i] < lst2[j]:
            lst.append(lst1[i])
            i += 1
        else:
            lst.append(lst2[j])
            j += 1

        if cnt == k:
            return (lst[k - 1] + lst[k]) * 0.5 if (len1 + len2) % 2 == 0 else lst[k]
        cnt += 1
    return None


def median_of_two_sorted_list2(lst1, lst2):
    def kth_small(lst1, lst2, i1, i2, k):
        len_lst1, len_lst2 = len(lst1), len(lst2)
        if i1 >= len_lst1: 
            return lst2[k - 1]
        if i2 >= len_lst2: 
            return lst1[k - 1]
        if k == 1:
            return min(lst1[i1], lst2[i2])
        if len_lst1 - i1 > len_lst2 - i2: 
            return kth_small(lst2, lst1, i2, i1, k)
        pa = min(len_lst1 - i1, k // 2)
        pb = k - pa
        return (kth_small(lst1, lst2, i1 + pa, i2, pb)
                if lst1[i1 + pa - 1] < lst2[i2 + pb - 1]
                else kth_small(lst1, lst2, i1, i2 + pb, pa))

    len_total = len(lst1) + len(lst2)
    return (kth_small(lst1, lst2, 0, 0, len_total // 2 + 1)
            if len_total % 2
            else 0.5 * (kth_small(lst1, lst2, 0, 0, len_total // 2) + kth_small(lst1, lst2, 0, 0, len_total // 2 + 1)))


if __name__ == '__main__':
    assert median_of_two_sorted_list1([], [2]) == 2
    assert median_of_two_sorted_list1([1], [2]) == 1.5
    assert median_of_two_sorted_list1([1], [2, 3]) == 2
    assert median_of_two_sorted_list1([0, 1], [2, 3]) == 1.5
    assert median_of_two_sorted_list1([1, 2, 3], [4, 5, 6, 7]) == 4
    assert median_of_two_sorted_list1([1, 2, 3], [4, 5, 6, 7, 8]) == 4.5
    assert median_of_two_sorted_list1([1, 3, 5, 21, 31], [2, 8, 16, 20, 22, 43]) == 16
    cProfile.run('median_of_two_sorted_list1([1, 3, 5, 21, 31], [2, 8, 16, 20, 22, 43])')

    assert median_of_two_sorted_list2([], [2]) == 2
    assert median_of_two_sorted_list2([1], [2]) == 1.5
    assert median_of_two_sorted_list2([1], [2, 3]) == 2
    assert median_of_two_sorted_list2([0, 1], [2, 3]) == 1.5
    assert median_of_two_sorted_list2([1, 2, 3], [4, 5, 6, 7]) == 4
    assert median_of_two_sorted_list2([1, 2, 3], [4, 5, 6, 7, 8]) == 4.5
    assert median_of_two_sorted_list2([1, 3, 5, 21, 31], [2, 8, 16, 20, 22, 43]) == 16
    cProfile.run('median_of_two_sorted_list2([1, 3, 5, 21, 31], [2, 8, 16, 20, 22, 43])')
