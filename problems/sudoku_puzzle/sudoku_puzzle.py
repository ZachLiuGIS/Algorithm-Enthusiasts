def is_valid_sudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    rows = [{} for i in range(9)]
    cols = [{} for j in range(9)]
    windows = [[{} for i in range(3)] for j in range(3)]
    for i in range(9):
        for j in range(9):
            v = board[i][j]
            if v == '.':
                continue

            if v in rows[i]:
                return False
            else:
                rows[i][v] = 1

            if v in cols[j]:
                return False
            else:
                cols[j][v] = 1

            if v in windows[i // 3][j // 3]:
                return False
            else:
                windows[i // 3][j // 3][v] = 1

    return True


if __name__ == '__main__':
    assert (is_valid_sudoku(
        [".87654321", "2........", "3........", "4........", "5........", "6........", "7........", "8........",
         "9........"]) == True)
