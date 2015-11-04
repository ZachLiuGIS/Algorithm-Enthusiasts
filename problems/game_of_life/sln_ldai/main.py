
def neighbors(cell):
    x, y = cell
    yield x - 1, y - 1
    yield x    , y - 1
    yield x + 1, y - 1
    yield x - 1, y
    yield x + 1, y
    yield x - 1, y + 1
    yield x    , y + 1
    yield x + 1, y + 1

def apply_iteration(board):
    new_board = set([])
    candidates = board.union(set(n for cell in board for n in neighbors(cell)))
    """print(candidates)"""
    for cell in candidates:
        count = sum((n in board) for n in neighbors(cell))
        if count == 3 or (count == 2 and cell in board):
            new_board.add(cell)
    return new_board

def display(state):
    output = ''
    board = [[0 for i in range(5)] for j in range(5)]
    for x,y in state:
        board[x][y] = "x"
    print (board)    
        
    

if __name__ == "__main__":
    '''test = {(0,1), (1,2), (2,0), (2,1), (2,2)}'''
    state = {(1,1), (2,2), (1,2), (2,1)}
    state = {(0,1), (1,1), (2,1)}
    number_of_iterations = 2
    for _ in range(number_of_iterations):
        state = apply_iteration(state)
    display(state)
