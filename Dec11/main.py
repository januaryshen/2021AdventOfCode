import numpy as np


class FlashingOctopus:
    def __init__(self):
        self.flashes = 0

    def check_surrounding(self, matrix, row, col):
        for row_s in range(row - 1, row + 2):
            for col_s in range(col - 1, col + 2):
                if row_s == row and col_s == col:
                    continue
                if matrix[row_s][col_s] >= 9:
                    matrix[row][col] = matrix[row][col] + 1
        return matrix

    def padding_reset(self, matrix) -> object:
        n, m = matrix.shape[0], matrix.shape[1]
        matrix[0] = 0
        matrix[n - 1] = 0
        matrix[:, 0] = 0
        matrix[:, m - 1] = 0
        return matrix

    def add_one_to_surroundings(self, matrix, row, col, this_round):
        matrix[row][col] = 0
        this_round.add((row, col))
        self.flashes += 1
        for row_s in range(row - 1, row + 2):
            for col_s in range(col - 1, col + 2):
                if row_s == row and col_s == col:
                    continue
                else:
                    if (row_s, col_s) not in this_round:
                        matrix[row_s][col_s] = matrix[row_s][col_s] + 1
                    if matrix[row_s][col_s] > 9:
                        matrix = self.add_one_to_surroundings(matrix, row_s, col_s, this_round)
        return matrix


def part1(inputData):
    matrix = [[*map(int, l[:-1])] for l in open(inputData)]
    matrix = np.array(matrix)
    padded_m = np.pad(matrix, [(1, 1), (1, 1)], 'constant')

    iteration = 100
    octopus = FlashingOctopus()

    for i in range(iteration):
        this_round = set()
        # start adding for cells
        padded_m = padded_m + 1
        for row in range(1, padded_m.shape[0] - 1):
            for col in range(1, padded_m.shape[1] - 1):
                if padded_m[row][col] > 9:
                    padded_m = octopus.add_one_to_surroundings(padded_m, row, col, this_round)

        # reset paddings to 0
        padded_m = octopus.padding_reset(padded_m)

    print(octopus.flashes)
    print(padded_m)


def part2(inputData):
    matrix = [[*map(int, l[:-1])] for l in open(inputData)]
    matrix = np.array(matrix)
    padded_m = np.pad(matrix, [(1, 1), (1, 1)], 'constant')

    octopus = FlashingOctopus()
    iteration = 0

    keep_looking = True
    while keep_looking is True:
        this_round = set()
        # start adding for cells
        padded_m = padded_m + 1
        for row in range(1, padded_m.shape[0] - 1):
            for col in range(1, padded_m.shape[1] - 1):
                if padded_m[row][col] > 9:
                    padded_m = octopus.add_one_to_surroundings(padded_m, row, col, this_round)

        # reset paddings to 0
        padded_m = octopus.padding_reset(padded_m)

        iteration += 1
        if np.array(padded_m).sum() == 0:
            keep_looking = False

    print(iteration)


if __name__ == "__main__":
    input_data = "./data.txt"
    # part1(input_data)
    part2(input_data)
    # a = [[1, 2], [3, 4]]
    # b = np.pad(a, [(1,1), (1,1)], 'constant')
    # print(b)
