from collections import defaultdict
from functools import reduce


def part1(inputData, polymer, iteration):
    polymer_dict = {}
    input_dots = [x.rstrip().split(" -> ") for x in open(inputData).readlines()]
    for x in input_dots:
        polymer_dict[x[0]] = x[1]

    polymer_list = [char for char in polymer]
    for iter in range(iteration):
        index_list = []
        value_list = []
        for i in range(len(polymer_list)-1):
            key = polymer_list[i] + polymer_list[i+1]
            if key in polymer_dict.keys():
                index_list.append(i)
                value_list.append(polymer_dict.get(key))

        num_to_insert = len(index_list)
        for pos in range(num_to_insert):
            index = index_list[num_to_insert - pos - 1]
            polymer_list.insert(index + 1, value_list[num_to_insert - pos - 1])

        # print(polymer_list)

    poly_count = {}
    for poly in polymer_list:
        if poly not in poly_count.keys():
            poly_count[poly] = 1
        else:
            poly_count[poly] = poly_count.get(poly) + 1

    print(poly_count)
    print(max(poly_count.values()) - min(poly_count.values()))


def part2(inputData, polymer):
    I = list(map(str.strip, open(inputData).readlines()))

    def parse_template(t):
        res = defaultdict(lambda: 0)

        for i in range(len(t) - 1):
            res[t[i] + t[i + 1]] += 1

        return res

    template = parse_template(polymer)
    rules = {p: i for p, i in (x.split(" -> ") for x in I)}

    def expand(s):
        res = defaultdict(lambda: 0)

        for key in s.keys():
            if key in rules:
                res[key[0] + rules[key]] += s[key]
                res[rules[key] + key[1]] += s[key]
            else:
                res[key] += 1

        return res

    def expand_n(n, t):
        return reduce(lambda s, _: expand(s), range(n), t)

    def count_elems(s):
        res = defaultdict(lambda: 0)

        for key in s:
            res[key[1]] += s[key]

        return res

    count = count_elems(expand_n(10, template))
    print("part1", max(count.values()) - min(count.values()))

    count = count_elems(expand_n(40, template))
    print("part2", max(count.values()) - min(count.values()))


if __name__ == "__main__":
    input_data = "./data.txt"
    polymer = "CFFPOHBCVVNPHCNBKVNV"
    part1(input_data, polymer, 10)
    # part 2 is from Reddit zndflxtyh at https://www.reddit.com/r/adventofcode/comments/rfzq6f/2021_day_14_solutions/
    part2(input_data, polymer)
