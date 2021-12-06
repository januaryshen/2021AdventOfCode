import numpy as np
import pandas as pd


def read_matrix(inputData):
    with open(inputData) as file:
        lines = file.readlines()
        num_seq = lines[0].split(",")
        num_seq = list(map(int, num_seq))

        counter = 1
        matrix_dict = {}
        matrix = []
        for i in range(2, len(lines)):
            if lines[i] == '\n':
                matrix_dict[counter] = np.matrix(matrix)
                counter += 1
                matrix = []
            else:
                a_row = lines[i][:-1].split(" ")
                a_row = [j for j in a_row if j]
                a_row = list(map(int, a_row))
                matrix.append(a_row)

    return num_seq, matrix_dict


def get_bingo_line(num_seq, matrix_dict):
    number_of_bingo_dict = {}
    crossed_matrix_dict = {}
    for i in range(len(matrix_dict)):
        target_matrix = np.matrix(matrix_dict.get(i))
        crossed_matrix = np.zeros(target_matrix.shape)
        for num in num_seq:
            indices = np.where(target_matrix == num)
            crossed_matrix[indices] = 1
            if 5 in crossed_matrix.sum(axis=1) or 5 in crossed_matrix.sum(axis=0):
                number_of_bingo_dict[i] = num
                crossed_matrix_dict[i] = crossed_matrix
                break
    return number_of_bingo_dict, crossed_matrix_dict


def part1(inputData):
    num_seq, matrix_dict = read_matrix(inputData)
    number_of_bingo_dict, crossed_matrix_dict = get_bingo_line(num_seq, matrix_dict)
    smallest_index = 100
    for bingo_number in number_of_bingo_dict.values():
        if num_seq.index(bingo_number) < smallest_index:
            smallest_index = num_seq.index(bingo_number)

    winning_matrix_index = list(number_of_bingo_dict.keys())[list(number_of_bingo_dict.values()).index(num_seq[smallest_index])]
    winning_matrix = matrix_dict.get(winning_matrix_index)
    crossed_matrix = crossed_matrix_dict.get(winning_matrix_index)
    bingo_number = number_of_bingo_dict.get(winning_matrix_index)

    print(winning_matrix)
    print(crossed_matrix)
    print(bingo_number)
    print(abs(np.multiply((crossed_matrix - 1), winning_matrix).sum()) * bingo_number)


def part2(inputData):
    num_seq, matrix_dict = read_matrix(inputData)
    number_of_bingo_dict, crossed_matrix_dict = get_bingo_line(num_seq, matrix_dict)
    largest_index = 0
    for bingo_number in number_of_bingo_dict.values():
        if num_seq.index(bingo_number) > largest_index:
            largest_index = num_seq.index(bingo_number)

    winning_matrix_index = list(number_of_bingo_dict.keys())[list(number_of_bingo_dict.values()).index(num_seq[largest_index])]
    winning_matrix = matrix_dict.get(winning_matrix_index)
    crossed_matrix = crossed_matrix_dict.get(winning_matrix_index)
    bingo_number = number_of_bingo_dict.get(winning_matrix_index)

    print(winning_matrix)
    print(crossed_matrix)
    print(bingo_number)
    print(abs(np.multiply((crossed_matrix - 1), winning_matrix).sum()) * bingo_number)


if __name__ == "__main__":
    input_data = "./data.txt"
    # part1(input_data)
    part2(input_data)
