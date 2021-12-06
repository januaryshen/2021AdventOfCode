import numpy as np
import pandas as pd


def part1(inputData):
    positionDict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}
    with open(inputData) as file:
        lines = file.readlines()
        for code in range(len(lines)):
            pos = 0
            for index in lines[code]:
                if index == "0":
                    positionDict[pos] = positionDict.get(pos) - 1
                elif index == "1":
                    positionDict[pos] = positionDict.get(pos) + 1
                pos += 1

        gamma_string = ""
        epsilon_string = ""
        for position in range(12):
            if positionDict.get(position) > 0:
                gamma_string += "1"
                epsilon_string += "0"
            else:
                gamma_string += "0"
                epsilon_string += "1"

        gamma = int(gamma_string, 2)
        epsilon = int(epsilon_string, 2)
        print(gamma_string)
        print(epsilon_string)
        print(gamma)
        print(epsilon)
        print(gamma * epsilon)


def part2(inputData):
    df = pd.read_csv(inputData, dtype=str, header=None)
    df.rename(columns={0: "digits"}, inplace=True)
    for pos in range(12):
        sumOfOne = df['digits'].apply(lambda x: int(x[pos])).sum()
        df['conditionMet'] = 0

        if sumOfOne >= df.shape[0] / 2:
            commonNumber = 1
        else:
            commonNumber = 0

        df['conditionMet'] = np.where(df['digits'].apply(lambda x: x[pos]) == str(commonNumber), 1, 0)
        if df.shape[0] - df['conditionMet'].sum() > 0:
            df = df[df['conditionMet'] != 0]
        else:
            break
        # print(pos, sumOfOne, df.shape, commonNumber)

    gamma = df['digits'].values[0]
    print(gamma, int(gamma, 2), df)

# epsilon
    df = pd.read_csv(inputData, dtype=str, header=None)
    df.rename(columns={0: "digits"}, inplace=True)
    for pos in range(12):
        sumOfOne = df['digits'].apply(lambda x: int(x[pos])).sum()
        df['conditionMet'] = 0

        if sumOfOne >= df.shape[0] / 2:
            commonNumber = 1
        else:
            commonNumber = 0

        df['conditionMet'] = np.where(df['digits'].apply(lambda x: x[pos]) == str(commonNumber), 1, 0)
        if df.shape[0] - df['conditionMet'].sum() > 0:
            df = df[df['conditionMet'] != 1]  # leave the unmet rows
        else:
            break
        # print(pos, sumOfOne, df.shape, commonNumber)

    epsilon = df['digits'].values[0]
    print(epsilon, int(epsilon, 2), df)
    print(int(gamma, 2) * int(epsilon, 2))


if __name__ == "__main__":
    input_data = "./data.txt"
    # part1(input_data)
    part2(input_data)
