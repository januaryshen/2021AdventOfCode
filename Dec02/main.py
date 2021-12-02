

def part1(inputData):
    with open(inputData) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        forward = 0
        depth = 0
        for command in lines:
            direction, number = command.split(" ")
            number = int(number)
            if direction == "forward":
                forward += number
            elif direction == "down":
                depth += number
            elif direction == "up":
                depth -= number

        print(forward, depth, forward * depth)


def part2(inputData):
    with open(inputData) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        forward = 0
        depth = 0
        aim = 0
        for command in lines:
            direction, number = command.split(" ")
            number = int(number)
            if direction == "forward":
                forward += number
                depth = depth + aim * number
            elif direction == "down":
                aim += number
            elif direction == "up":
                aim -= number

        print(forward, depth, forward * depth)


if __name__ == "__main__":
    input_data = "./data.txt"
    part1(input_data)
    part2(input_data)