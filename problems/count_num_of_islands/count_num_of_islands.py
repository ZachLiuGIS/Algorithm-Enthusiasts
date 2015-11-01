# This solution uses two loops.
# First, count separate island on each row
# Because island can be connected vertically, the first round of counting is redundant.
# Second, use another loop to reduce redundant counts.
# If an row island is connected with an island below, the total count will be reduced by one.


def count_land_loop(data):
    n_row, n_col = len(data), len(data[0])
    count = 0

    # count horizontal for row islands
    for i in range(n_row):
        j = 0
        while j < n_col:
            if data[i][j] == 0:
                j += 1
                continue
            else:
                if j == n_col - 1 or data[i][j+1] == 0:
                    count += 1
                j += 1

    # reduce vertical down for redundant counts
    for i in range(n_row - 1):
        j = 0
        while j < n_col:
            if data[i+1][j] == 0:
                j += 1
                continue
            else:
                if data[i][j] == 0:
                    j += 1
                    continue
                else:
                    count -= 1
                    while data[i][j] == 1 and data[i+1][j] == 1:
                        j += 1
                        if j == n_col:
                            break
    return count


# This solution uses recursion
# Find a new island piece first, then use recursive function count_connected to get all pieces of the island
# all pieces that are counted are stored so they won't be counted again.

def count_land_recursive(data):
    count = {
        "count": 0,
        "counted": set()
    }

    def count_connected(i, j):
        if (i, j) in count["counted"]:
            return
        count["counted"].add((i, j))

        if j != n_col - 1:
            if data[i][j+1] != 0:
                count_connected(i, j+1)
        if i != n_row - 1:
            if data[i+1][j] != 0:
                count_connected(i+1, j)
        if j != 0:
            if data[i][j-1] != 0:
                count_connected(i, j-1)
        if i != 0:
            if data[i-1][j] != 0:
                count_connected(i-1, j)

    n_row, n_col = len(data), len(data[0])

    for i in range(n_row):
        for j in range(n_col):
            if (i, j) not in count['counted'] and data[i][j] == 1:
                count["count"] += 1
                count_connected(i, j)

    return count["count"]
