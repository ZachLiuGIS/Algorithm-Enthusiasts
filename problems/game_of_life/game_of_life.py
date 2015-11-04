import time
import copy


class GameOfLife(object):

    def __init__(self, grid):
        self.grid = grid
        self.n_row = len(grid)
        self.n_col = len(grid[0])

    def update_grid(self):

        # For each update, have to create a new grid

        new_grid = copy.deepcopy(self.grid)

        for i in range(self.n_row):
            for j in range(self.n_col):
                if self.is_alive(i, j):
                    if self.will_keep_living(i, j):
                        new_grid[i][j] = 1
                    else:
                        new_grid[i][j] = 0
                else:
                    if self.will_relive(i, j):
                        # print(i, j, self.num_of_live_neighbor(i, j))
                        new_grid[i][j] = 1
                    else:
                        new_grid[i][j] = 0
        self.grid = copy.deepcopy(new_grid)

    def is_alive(self, i, j):
        return self.grid[i][j] == 1

    def will_relive(self, i, j):
        return self.num_of_live_neighbor(i, j) == 3

    def will_keep_living(self, i, j):
        return self.is_alive(i, j) and (self.num_of_live_neighbor(i, j) == 2 or self.num_of_live_neighbor(i, j) == 3)

    def num_of_live_neighbor(self, m, n):
        count = 0
        grid = self.grid

        for y in [m-1, m, m+1]:
            for x in [n-1, n, n+1]:
                if y == m and x == n:
                    continue
                elif 0 <= y < self.n_row and 0 <= x < self.n_col:
                    if grid[y][x] == 1:
                        count += 1
        return count

    def is_active(self):
        return True

    def start(self):
        while self.is_active():
            self.update_grid()
            self.print_grid()
            time.sleep(1)

    def print_grid(self):
        for i in range(self.n_row):
            print(self.grid[i])
        print("-----------------------")


if __name__ == '__main__':

    grid1 = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]

    grid2 = [
        [0, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]

    game = GameOfLife(grid2)
    game.start()
