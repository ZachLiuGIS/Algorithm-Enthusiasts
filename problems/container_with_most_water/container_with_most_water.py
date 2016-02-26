import cProfile


def max_area_brute_force(height):
    max_ = 0
    for i in range(len(height)):
        if i > 0 and height[i] <= min(height[0:i]):
            continue
        for j in range(i, len(height)):
            area = (j - i) * min(height[i], height[j])
            if area > max_:
                max_ = area
    return max_


def max_area(height):
    l = max_ = 0
    r = len(height) - 1
    while not l == r:
        if height[l] < height[r]:
            max_ = max(max_, (r - l) * height[l])
            l += 1
        else:
            max_ = max(max_, (r - l) * height[r])
            r -= 1
    return max_

if __name__ == '__main__':
    assert max_area([1, 2]) == 1
    assert max_area([2, 2]) == 2
    assert max_area([3, 2, 3, 4]) == 9
    assert max_area([21, 20, 2, 3, 1]) == 20

    cProfile.run('max_area([21, 20, 2, 3, 1])')
