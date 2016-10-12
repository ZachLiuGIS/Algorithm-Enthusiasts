def max_intersection_segment(segs):
    segs = sorted(segs, key=lambda item: item[0])
    max_seg = None
    max_interection = 0
    i = 0
    active_segs = {}
    while i < len(segs):
        current = segs[i]
        removed_keys = []
        for seg in active_segs:
            if seg[1] >= current[0]:
                active_segs[(seg[0], seg[1])] += 1
            elif active_segs[(seg[0], seg[1])] > max_interection:
                max_interection = active_segs[(seg[0], seg[1])]
                max_seg = [seg[0], seg[1]]
                removed_keys.append((seg[0], seg[1]))
        for key in removed_keys:
            del active_segs[key]
        active_segs[(current[0], current[1])] = len(active_segs)
        i += 1
    if active_segs[(segs[-1][0], segs[-1][1])] > max_interection:
        return segs[-1]
    return max_seg


if __name__ == "__main__":
    assert (max_intersection_segment([[1, 3], [2, 4], [7, 8], [4, 5]]) == [2, 4])
    assert (max_intersection_segment([[1, 3], [2, 4], [7, 8], [4, 5]]) == [2, 4])
    assert (max_intersection_segment([[3, 7], [4, 6],
                                      [1, 3], [2, 5],
                                      [5, 8], [7, 9],
                                      [10, 11], [10, 12]]) == [3, 7])
