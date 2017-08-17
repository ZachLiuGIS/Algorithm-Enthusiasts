import sys


def jump_game_dfs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ret = 0
    len_n = len(nums)
    if len_n == 1:
        return 0

    def dfs(n, idx):
        if idx == len_n - 1:
            return n
        if nums[idx] == 0:
            return sys.maxsize
        return min(dfs(n + 1, idx + i + 1) for i in range(nums[idx]) if idx + i + 1 < len_n)

    return dfs(0, 0)


def jump_game_bfs(nums):
    stack = []
    item_set = set()
    stack.append((0, 0))
    while stack:
        item = stack.pop()
        if item[0] > len(nums) - 1:
            return item[1]
        if nums[item[0]] == 0:
            continue

        for i in range(nums[item[0]]):
            if item[0] + i + 1 == len(nums) - 1:
                return item[1] + 1
            if item[0] + i + 1 in item_set:
                continue
            item_set.add(item[0] + i + 1)
            stack.insert(0, (item[0] + i + 1, item[1] + 1))
    return None


def jump_game(nums):
    len_n = len(nums)
    end = 0
    start = 0
    step = 0

    while end < len_n - 1:
        step += 1
        maxend = end + 1
        for i in range(start, end + 1):
            if i + nums[i] >= len_n - 1:
                return step
            maxend = max(maxend, i + nums[i])
        start, end = end + 1, maxend
    return step


if __name__ == '__main__':
    print(jump_game_bfs([9, 7, 9, 4, 8, 1, 6, 1, 5, 6, 2, 1, 7, 9, 0]))
    print(jump_game_bfs([6, 2, 6, 1, 7, 9, 3, 5, 3, 7, 2, 8, 9, 4, 7, 7, 2, 2, 8, 4, 6, 6, 1, 3]))
    print(jump_game_bfs([1, 2, 0, 1]))
    print(jump_game_bfs([2, 3, 1, 1, 4]))
    print(jump_game_dfs([9, 7, 9, 4, 8, 1, 6, 1, 5, 6, 2, 1, 7, 9, 0]))
    print(jump_game_dfs([6, 2, 6, 1, 7, 9, 3, 5, 3, 7, 2, 8, 9, 4, 7, 7, 2, 2, 8, 4, 6, 6, 1, 3]))
    print(jump_game_dfs([1, 2, 0, 1]))
    print(jump_game_dfs([2, 3, 1, 1, 4]))
    print(jump_game([9, 7, 9, 4, 8, 1, 6, 1, 5, 6, 2, 1, 7, 9, 0]))
    print(jump_game([6, 2, 6, 1, 7, 9, 3, 5, 3, 7, 2, 8, 9, 4, 7, 7, 2, 2, 8, 4, 6, 6, 1, 3]))
    print(jump_game([1, 2, 0, 1]))
    print(jump_game([2, 3, 1, 1, 4]))
