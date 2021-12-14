import numpy as np


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
