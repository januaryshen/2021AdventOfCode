

def part1(inputData):
    f = open(inputData, "r")
    current_depth = 0
    increase_counter = 0
    decrease_counter = 0
    for i in f:
        if int(i) > current_depth:
            increase_counter += 1
        elif int(i) < current_depth:
            decrease_counter += 1
        current_depth = int(i)
    f.close()

    print(increase_counter - 1, decrease_counter)


def part2(inputData):
    with open(inputData) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

        prev_sum = 0
        increase_counter = 0
        decrease_counter = 0
        for j in range(len(lines) - 2):
            pos1 = int(lines[j])
            pos2 = int(lines[j + 1])
            pos3 = int(lines[j + 2])
            pos_sum = pos1 + pos2 + pos3

            if pos_sum > prev_sum:
                increase_counter += 1
            elif pos_sum < prev_sum:
                decrease_counter += 1
            prev_sum = pos_sum

    print(increase_counter - 1, decrease_counter)


if __name__ == "__main__":
    input_data = "./data.txt"
    part1(input_data)
    part2(input_data)