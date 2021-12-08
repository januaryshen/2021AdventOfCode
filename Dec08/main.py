import numpy as np
from collections import defaultdict


def get_combination_dict(combination):
    combination_dict = {}
    for item in combination:
        if len(item) not in combination_dict.keys():
            combination_dict[len(item)] = [item]
        else:
            combination_dict[len(item)].append(item)
    return combination_dict


def get_location_dict(combination_dict):
    # ** position mapping **
    #        "bo"
    #    "po"    "mo"
    #        "fo"
    #    "de"    "te"
    #        "ne"

    location_dict = {}
    for letter in str(combination_dict.get(2)[0]):  # display 1
        location_dict[letter] = {"mo", "te"}
    for letter in str(combination_dict.get(3)[0]):  # display 7
        if letter not in location_dict.keys():
            location_dict[letter] = {"bo"}
    for letter in str(combination_dict.get(4)[0]):  # display 4
        location_dict[letter] = {"po", "fo"}
    possible_2 = set(combination_dict.get(5)[0])  # display 2, 3, 5
    possible_3 = set(combination_dict.get(5)[1])
    possible_5 = set(combination_dict.get(5)[2])
    common_three = possible_2.intersection(possible_3, possible_5)
    for letter in common_three:
        if letter not in location_dict.keys():
            location_dict[letter] = {"ne"}
        else:
            if len(location_dict.get(letter)) == 2:
                location_dict[letter] = {"fo"}
    for letter in str(combination_dict.get(4)[0]):  # update position "po"
        if len(location_dict.get(letter)) == 2 and letter not in set(combination_dict.get(2)[0]):
            location_dict[letter] = {"po"}

    possible_6 = set(combination_dict.get(6)[0])  # display 6, 9, 0
    possible_9 = set(combination_dict.get(6)[1])
    possible_0 = set(combination_dict.get(6)[2])
    common_four = possible_6.intersection(possible_9, possible_0)
    for letter in common_four:
        if letter in set(combination_dict.get(2)[0]):
            location_dict[letter] = {"te"}
    for letter in str(combination_dict.get(2)[0]):  # update position "mo"
        if len(location_dict.get(letter)) == 2:
            location_dict[letter] = {"mo"}
    for letter in set(combination_dict.get(7)[0]):
        if letter not in location_dict.keys():
            location_dict[letter] = {"de"}
    return location_dict


def get_digit_mapping_dict():
    mapping_dict = {}
    # mapping_dict[1] = {"mo", "te"}
    # mapping_dict[2] = {"bo", "mo", "fo", "de", "ne"}
    # mapping_dict[3] = {"bo", "mo", "fo", "te", "ne"}
    # mapping_dict[4] = {"po", "fo", "mo", "te"}
    # mapping_dict[5] = {"bo", "po", "fo", "te", "ne"}
    # mapping_dict[6] = {"bo", "po", "fo", "de", "ne", "te"}
    # mapping_dict[7] = {"bo", "mo", "te"}
    # mapping_dict[8] = {"bo", "po", "mo", "fo", "de", "te", "ne"}
    # mapping_dict[9] = {"bo", "po", "mo", "fo", "te", "ne"}
    # mapping_dict[0] = {"bo", "po", "mo", "de", "te", "ne"}
    mapping_dict[frozenset(["mo", "te"])] = 1
    mapping_dict[frozenset(["bo", "mo", "fo", "de", "ne"])] = 2
    mapping_dict[frozenset(["bo", "mo", "fo", "te", "ne"])] = 3
    mapping_dict[frozenset(["po", "mo", "fo", "te"])] = 4
    mapping_dict[frozenset(["bo", "po", "fo", "te", "ne"])] = 5
    mapping_dict[frozenset(["bo", "po", "fo", "de", "te", "ne"])] = 6
    mapping_dict[frozenset(["bo", "mo", "te"])] = 7
    mapping_dict[frozenset(["bo", "po", "mo", "fo", "de", "te", "ne"])] = 8
    mapping_dict[frozenset(["bo", "po", "mo", "fo", "te", "ne"])] = 9
    mapping_dict[frozenset(["bo", "po", "mo", "de", "te", "ne"])] = 0
    return mapping_dict


def part1(inputData):
    lines = open(inputData, 'r').read().split("\n")
    counter = 0
    for line in lines:
        digits = line.split(" | ")[1]
        digits = digits.split(" ")
        for digit in digits:
            if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:   # for digit 1, 4, 7, 8
                counter += 1
    print(counter)


def part2(inputData):
    lines = open(inputData, 'r').read().split("\n")
    counter = 0
    for line in lines:
        digits = line.split(" | ")
        combination = digits[0].split(" ")
        target = digits[1].split(" ")

        combination_dict = get_combination_dict(combination)
        location_dict = get_location_dict(combination_dict)
        digit_mapping_dict = get_digit_mapping_dict()

        string_target = ""
        for digit in target:
            number = set()
            for i in digit:
                number.update(location_dict.get(i))  # get the location needed for this digit
            string_target = string_target + str(digit_mapping_dict.get(frozenset(list(number))))
        counter += int(string_target)
    print(counter)


if __name__ == "__main__":
    input_data = "./data.txt"
    # part1(input_data)
    part2(input_data)