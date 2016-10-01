import sys


def minimum_sum_partition(lst):
    def find_min_rec(lst, sum_calculated, sum_total):
        if not hasattr(find_min_rec, 'result'):
            find_min_rec.result = []
        if len(lst) == 0:
            return abs((sum_total - sum_calculated) - sum_calculated)

        if find_min_rec(lst[:-1], sum_calculated + lst[-1], sum_total) <= find_min_rec(lst[:-1], sum_calculated, sum_total):
            find_min_rec.result += [lst[-1]]
            return find_min_rec(lst[:-1], sum_calculated + lst[-1], sum_total)
        return find_min_rec(lst[:-1], sum_calculated, sum_total)

    total = sum(lst)
    f = find_min_rec
    find_min_rec(lst, 0, total)
    return find_min_rec(lst, 0, total)


def minimum_sum_partition_dp(lst):
    total = sum(lst)
    len_lst = len(lst)

    mx = [[False] * (total + 1) for i in range(len_lst + 1)]

    for i in range(len_lst + 1):
        mx[i][0] = True
    for j in range(1, total + 1):
        mx[0][j] = False
    for i in range(1, len_lst + 1):
        for j in range(1, total + 1):
            mx[i][j] = mx[i-1][j]
            if lst[i - 1] <= j:
                mx[i][j] = not mx[i-1][j-lst[i-1]]

    diff = 0

    for j in range(total//2, -1, -1):
        if mx[len_lst][j]:
            diff = total-2*j
            break
    return diff

if __name__ == '__main__':
    print(minimum_sum_partition_dp([4, 2, 9, 5, 10]))
    print(minimum_sum_partition([4, 2, 9, 5, 10]))
