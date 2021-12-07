import numpy as np
from collections import defaultdict


def incremental_fuel(distance):
    if distance == 0:
        return 0
    else:
        return incremental_fuel(distance - 1) + distance


def part1(inputData):
    input = [int(x) for x in open(inputData, 'r').read().split(',')]
    dist_dict = {}
    for point in range(min(input), max(input) + 1):
        dist = 0
        for i in sorted(input):
            dist += abs(point - i)
        dist_dict[point] = dist

    print(min(dist_dict.values()))


def part2(inputData):
    input = [int(x) for x in open(inputData, 'r').read().split(',')]
    dist_dict = {}
    for point in range(min(input), max(input) + 1):
        dist = 0
        for i in sorted(input):
            dist += abs(point - i) * (abs(point - i) + 1) / 2   # using recursive calculation will exceed max recursive depth in python
        dist_dict[point] = dist

    print(min(dist_dict.values()))


if __name__ == "__main__":
    input_data = "./data.txt"
    # part1(input_data)
    part2(input_data)
    # print(incremental_fuel(6))