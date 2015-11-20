import itertools


def rotate_matrix(matrix, degree):
    length = len(matrix)
    new_matrix = [[0 for i in range(length)] for j in range(length)]

    if degree % 360 == 90:
        for i, j in itertools.product(range(length), range(length)):
            new_matrix[j][length - i - 1] = matrix[i][j]

    elif degree % 360 == 180:
        for i, j in itertools.product(range(length), range(length)):
            new_matrix[length - i - 1][length - j - 1] = matrix[i][j]

    elif degree % 360 == 270:
        for i, j in itertools.product(range(length), range(length)):
            new_matrix[length - j - 1][i] = matrix[i][j]

    return new_matrix


def rotate_matrix_in_place(matrix):
    length = len(matrix)

    for i in range(int(length / 2)):
        start, end = i, length - i
        # print(start, end)
        for j in range(start, end - 1):
            top_left = matrix[start][j]
            matrix[start][j] = matrix[length - 1 - j][start]
            matrix[length - 1 - j][start] = matrix[length - 1 - start][length - 1 - j]
            matrix[length - 1 - i][length - 1 - j] = matrix[j][length - 1 - start]
            matrix[j][length - 1 - i] = top_left
    # print(matrix)
    return matrix


if __name__ == '__main__':
    m1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [2, 3, 4, 5],
        [3, 4, 5, 6]
    ]

    m1_90 = [
        [3, 2, 5, 1],
        [4, 3, 6, 2],
        [5, 4, 7, 3],
        [6, 5, 8, 4]
    ]

    m1_180 = [
        [6, 5, 4, 3],
        [5, 4, 3, 2],
        [8, 7, 6, 5],
        [4, 3, 2, 1]
    ]

    m1_neg90 = [
        [4, 8, 5, 6],
        [3, 7, 4, 5],
        [2, 6, 3, 4],
        [1, 5, 2, 3]
    ]
    assert rotate_matrix(m1, 90) == m1_90
    assert rotate_matrix(m1, 180) == m1_180
    assert rotate_matrix(m1, -90) == m1_neg90

    assert rotate_matrix_in_place(m1) == m1_90
    assert rotate_matrix_in_place(m1) == m1_180
    assert rotate_matrix_in_place(m1) == m1_neg90
