import numpy as np
from collections import defaultdict


def get_matrix(inputData):
    matrix = []
    with open(inputData, 'r') as f:
        data = f.read().split()
        for row in data:
            row = [int(char) for char in row]
            matrix.append(row)
    target_matrix = np.array(matrix)
    return target_matrix


def get_center_low_points(matrix):
    counter = 0
    for row in range(1, matrix.shape[0] - 1):
        for col in range(1, matrix.shape[1] - 1):
            self = matrix.item((row, col))
            up = matrix[row - 1, col]
            down = matrix[row + 1, col]
            left = matrix[row, col - 1]
            right = matrix[row, col + 1]
            if self < min(up, down, left, right):
                counter += self + 1
    return counter


def get_edge_low_points(matrix):
    counter = 0

    # top row
    row = 0
    for col in range(1, matrix.shape[1] - 1):
        self = matrix.item((row, col))
        down = matrix[row + 1, col]
        left = matrix[row, col - 1]
        right = matrix[row, col + 1]
        if self < min(down, left, right):
            print(self, row, col)
            counter += self + 1

    # bottom row
    row = matrix.shape[0] - 1
    for col in range(1, matrix.shape[1] - 1):
        self = matrix.item((row, col))
        up = matrix[row - 1, col]
        left = matrix[row, col - 1]
        right = matrix[row, col + 1]
        if self < min(up, left, right):
            counter += self + 1

    # most left col
    col = 0
    for row in range(1, matrix.shape[0] - 1):
        self = matrix.item((row, col))
        up = matrix[row - 1, col]
        down = matrix[row + 1, col]
        right = matrix[row, col + 1]
        if self < min(up, down, right):
            counter += self + 1

    # most right col
    col = matrix.shape[1] - 1
    for row in range(1, matrix.shape[0] - 1):
        self = matrix.item((row, col))
        up = matrix[row - 1, col]
        down = matrix[row + 1, col]
        left = matrix[row, col - 1]
        if self < min(up, down, left):
            counter += self + 1

    return counter


def part1(inputData):
    matrix = get_matrix(inputData)
    counter = 0
    counter += get_center_low_points(matrix)
    counter += get_edge_low_points(matrix)
    print(counter)


def part2(inputData):
    matrix = get_matrix(inputData)
    non_nine_matrix = np.zeros(matrix.shape)
    non_nine_matrix[matrix != 9] = 1

    class Solution:
        def __init__(self):
            self.island_1 = 0
            self.island_2 = 0
            self.island_3 = 0

        def num_of_basin(self, matrix):
            island_num = 0

            for row in range(matrix.shape[0]):
                for col in range(matrix.shape[1]):
                    if matrix[row][col] == 1:
                        self.dfs(matrix, row, col, 1)
                        island_num += 1

            return island_num

        def dfs(self, matrix, row, col, island_size):
            direction = [[1, 0], [0, -1], [0, 1], [-1, 0]]
            matrix[row][col] = 0
            for dir in direction:
                nr = row + dir[0]
                nc = col + dir[1]
                if 0 <= nr < matrix.shape[0] and 0 <= nc < matrix.shape[1]:
                    if matrix[nr][nc] == 1:
                        island_size += 1
                        self.dfs(matrix, nr, nc, island_size)
            if island_size > self.island_1:
                self.island_3 = self.island_2
                self.island_2 = self.island_1
                self.island_1 = island_size
            elif island_size > self.island_2:
                self.island_3 = self.island_2
                self.island_2 = island_size
            elif island_size > self.island_3:
                self.island_3 = island_size

    sol = Solution()
    print(sol.num_of_basin(non_nine_matrix))
    print(sol.island_1)
    print(sol.island_2)
    print(sol.island_3)
    print(sol.island_1 * sol.island_2 * sol.island_3)

    # print(island_num, island_1, island_2, island_3, island_1 * island_2 * island_3)


if __name__ == "__main__":
    input_data = "./data.txt"
    # part1(input_data)
    # part2(input_data)  # My part2 code is incorrect

    # Part 2: Modified input from Reddit user lbm364dl at https://www.reddit.com/r/adventofcode/comments/rca6vp/2021_day_9_solutions/
    grid = [[*map(int, l[:-1])] for l in open('./data.txt')]
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # order does not matter
    n, m = len(grid), len(grid[0])
    visited = set()


    def is_outside(y, x):
        return not (0 <= y < n and 0 <= x < m)


    def is_low_point(y, x):
        return all(is_outside(y + dy, x + dx) or grid[y + dy][x + dx] > grid[y][x] for dy, dx in delta)


    def dfs(y, x):
        if is_outside(y, x) or grid[y][x] == 9 or (y, x) in visited:
            return 0

        visited.add((y, x))
        return 1 + sum(dfs(y + dy, x + dx) for dy, dx in delta)


    lows = [(y, x) for y in range(n-1) for x in range(m-1) if is_low_point(y, x)]
    basins = sorted([dfs(y, x) for y, x in lows])

    # print('Star 1:', sum(grid[y][x] + 1 for y, x in lows))
    print('Star 2:', basins[-1] * basins[-2] * basins[-3])
    print(basins[-1], basins[-2], basins[-3])
