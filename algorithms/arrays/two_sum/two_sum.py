def two_sum_brute_force(arr, target):
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return i+1, j+1
    return None


def two_sum_dict(arr, target):
    table = {}
    for i in range(len(arr)):
        if target - arr[i] in table:
            return table[target - arr[i]] + 1, i + 1
        table[arr[i]] = i
    return None

