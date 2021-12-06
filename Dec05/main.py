import numpy as np
import pandas as pd


def part1(inputData):
    with open(inputData) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        matrix = np.zeros((999, 999), dtype=int)

        for line in lines:
            command = line.split(" -> ")
            start_command = command[0].split(",")
            start_command = list(map(int, start_command))
            end_command = command[1].split(",")
            end_command = list(map(int, end_command))

            start_x, start_y = start_command[0], start_command[1]
            end_x, end_y = end_command[0], end_command[1]

            if start_x == end_x:
                for i in range(min(start_y, end_y), max(start_y, end_y) + 1):
                    matrix[start_x, i] = matrix[start_x, i] + 1
            elif start_y == end_y:
                for i in range(min(start_x, end_x), max(start_x, end_x) + 1):
                    matrix[i, start_y] = matrix[i, start_y] + 1

    indices = np.where(matrix > 1)
    counter_matrix = np.zeros(matrix.shape)
    counter_matrix[indices] = 1
    print(counter_matrix.sum())


def part2(inputData):
    with open(inputData) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        matrix = np.zeros((999, 999), dtype=int)

        for line in lines:
            command = line.split(" -> ")
            start_command = command[0].split(",")
            start_command = list(map(int, start_command))
            end_command = command[1].split(",")
            end_command = list(map(int, end_command))

            start_x, start_y = start_command[0], start_command[1]
            end_x, end_y = end_command[0], end_command[1]
            if start_x == end_x:
                for i in range(min(start_y, end_y), max(start_y, end_y) + 1):
                    matrix[start_x, i] = matrix[start_x, i] + 1
            elif start_y == end_y:
                for i in range(min(start_x, end_x), max(start_x, end_x) + 1):
                    matrix[i, start_y] = matrix[i, start_y] + 1
            else:
                if end_x > start_x:
                    if end_y > start_y:
                        for i in range(end_x - start_x + 1):
                            matrix[start_x + i, start_y + i] = matrix[start_x + i, start_y + i] + 1
                    else:
                        for i in range(end_x - start_x + 1):
                            matrix[start_x + i, start_y - i] = matrix[start_x + i, start_y - i] + 1
                else:
                    if end_y > start_y:
                        for i in range(start_x - end_x + 1):
                            matrix[start_x - i, start_y + i] = matrix[start_x - i, start_y + i] + 1
                    else:
                        for i in range(start_x - end_x + 1):
                            matrix[start_x - i, start_y - i] = matrix[start_x - i, start_y - i] + 1

    indices = np.where(matrix > 1)
    counter_matrix = np.zeros(matrix.shape)
    counter_matrix[indices] = 1
    print(counter_matrix.sum())


if __name__ == "__main__":
    input_data = "./data.txt"
    # part1(input_data)
    part2(input_data)
