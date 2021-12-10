import statistics

chunk_dict = {"}": "{", ">": "<", ")": "(", "]": "["}
corrupted_lines = {}
incomplete_lines = {}

def get_corrupted_lines(chunk_string, line):
    queue = []
    chunk_length = len(chunk_string)
    chunk_counter = 0
    for chunk in chunk_string:
        chunk_counter += 1
        if chunk in ["<", "[", "{", "("]:
            queue.append(chunk)
            if chunk_counter == chunk_length:  # incomplete chunk (BE AWARE OF THIS SITUATION)
                incomplete_lines[line] = queue
        else:
            opening_chunk = chunk_dict.get(chunk)
            if queue[-1] == opening_chunk:
                queue.pop()
                if len(queue) == 0 and chunk_counter < chunk_length:  # finished chunk. None in this input
                    continue
                elif len(queue) > 0 and chunk_counter == chunk_length:  # incomplete chunk
                    incomplete_lines[line] = queue
                    break
            else:
                corrupted_lines[line] = chunk  # corrupted chunk
                break


def part1(inputData):
    input = [l.rstrip() for l in open(inputData)]

    for line in range(len(input)):
        chunk_string = input[line]
        get_corrupted_lines(chunk_string, line)

    counter_25137 = 0
    counter_1197 = 0
    counter_57 = 0
    counter_3 = 0
    for value in corrupted_lines.values():
        if value == ">":
            counter_25137 += 1
        elif value == "}":
            counter_1197 += 1
        elif value == "]":
            counter_57 += 1
        elif value == ")":
            counter_3 += 1

    print(corrupted_lines)
    print(counter_3 * 3 + counter_57 * 57 + counter_1197 * 1197 + counter_25137 * 25137)


def part2(input_data):
    part1(input_data)
    score_dict = {}
    for k, v in incomplete_lines.items():
        score = 0
        for chunk in v[::-1]:
            closing_chunk = list(chunk_dict.keys())[list(chunk_dict.values()).index(chunk)]
            if closing_chunk == ")":
                score = score * 5 + 1
            elif closing_chunk == "]":
                score = score * 5 + 2
            elif closing_chunk == "}":
                score = score * 5 + 3
            elif closing_chunk == ">":
                score = score * 5 + 4
        score_dict[k] = score

    print(score_dict)
    print(statistics.median(score_dict.values()))


if __name__ == "__main__":
    input_data = "./data.txt"
    # part1(input_data)
    part2(input_data)