import numpy as np
from collections import defaultdict


def part1(inputData):
    with open(inputData) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        lines = lines[0].split(",")
        lines = list(map(int, lines))
        lantern_fish = np.array(lines)
        day = 0
        while day < 80:
            # print(lantern_fish)
            lantern_fish = lantern_fish - 1
            zeros = np.count_nonzero(lantern_fish == -1)
            new_fishes = np.repeat(8, zeros, axis=0)
            lantern_fish[lantern_fish == -1] = 6
            lantern_fish = np.concatenate((lantern_fish, new_fishes), axis=0)
            day += 1
        print(lantern_fish.shape)


def part2(inputData):
    school = [int(x) for x in open(inputData, 'r').read().split(',')]
    fish_dict = {}
    fish_dict = defaultdict(lambda: 0, fish_dict)
    for fish in school:
        fish_dict[fish] = fish_dict.get(fish, 0) + 1

    day = 0
    while day < 256:
        # print(fish_dict)
        fish_dict[-1] = fish_dict.get(0, 0)
        fish_dict[0] = fish_dict.get(1, 0)
        fish_dict[1] = fish_dict.get(2, 0)
        fish_dict[2] = fish_dict.get(3, 0)
        fish_dict[3] = fish_dict.get(4, 0)
        fish_dict[4] = fish_dict.get(5, 0)
        fish_dict[5] = fish_dict.get(6, 0)
        fish_dict[6] = fish_dict.get(-1, 0) + fish_dict.get(7, 0)
        fish_dict[7] = fish_dict.get(8, 0)
        fish_dict[8] = fish_dict.get(-1, 0)
        day += 1
    print(sum(fish_dict.values()) - fish_dict.get(-1))


if __name__ == "__main__":
    input_data = "./data.txt"
    # part1(input_data)
    part2(input_data)
