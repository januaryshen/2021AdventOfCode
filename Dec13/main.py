import pandas as pd
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)


def fold_x(df, param):
    df['x'] = df['x'].apply(lambda i: i if int(i) < param else int(i) - 2*(int(i)-param))
    df = df[df['x'] != param]
    df.drop_duplicates(inplace=True)
    return df


def fold_y(df, param):
    df['y'] = df['y'].apply(lambda i: i if int(i) < param else int(i) - 2*(int(i)-param))
    df = df[df['y'] != param]
    df.drop_duplicates(inplace=True)
    return df


def part1(inputData):
    input_dots = [x.rstrip().split(",") for x in open(inputData).readlines()]
    input_dots = [(int(x[0]), int(x[1])) for x in input_dots]
    df = pd.DataFrame(input_dots, columns=['x', 'y'])

    param = 655
    df['x'] = df['x'].apply(lambda i: i if int(i) < param else int(i) - 2*(int(i)-param))
    df = df[df['x'] != param]
    # df['y'] = df['y'].apply(lambda i: i if int(i) < param else int(i) - 2*(int(i)-param))
    # df = df[df['y'] != param]
    print(df.shape)
    df.drop_duplicates(inplace=True)
    print(df.shape)


def part2(inputData):
    input_dots = [x.rstrip().split(",") for x in open(inputData).readlines()]
    input_dots = [(int(x[0]), int(x[1])) for x in input_dots]
    df = pd.DataFrame(input_dots, columns=['x', 'y'])

    df = fold_x(df, 655)
    df = fold_y(df, 447)
    df = fold_x(df, 327)
    df = fold_y(df, 223)
    df = fold_x(df, 163)
    df = fold_y(df, 111)
    df = fold_x(df, 81)
    df = fold_y(df, 55)
    df = fold_x(df, 40)
    df = fold_y(df, 27)
    df = fold_y(df, 13)
    df = fold_y(df, 6)

    new_df = pd.DataFrame()
    new_df['x'] = df['y']
    new_df['y'] = df['x']

    coordinates = new_df.values.tolist()
    # max_num = max(coordinates)
    # print(max(max_num))
    zero_matrix = np.zeros([6, 39])
    for i in coordinates:
        zero_matrix[i[0]][i[1]] = 1
    print(zero_matrix)
    print(zero_matrix.shape)


if __name__ == "__main__":
    input_data = "./data.txt"
    # part1(input_data)
    part2(input_data)
