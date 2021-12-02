PUZZLE_INPUT_FILE = "puzzle_input.txt"


def parse_step(step_str):
    split = step_str.split()
    return split[0], int(split[1])


if __name__ == "__main__":
    puzzle_input = open(PUZZLE_INPUT_FILE, "r").readlines()

    horizontal = 0
    depth = 0

    for step in puzzle_input:
        command, x = parse_step(step)
        if command == "forward":
            horizontal += x
        elif command == "up":
            depth -= x
        elif command == "down":
            depth += x

    print(horizontal*depth)
