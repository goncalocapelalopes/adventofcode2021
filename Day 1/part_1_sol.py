PUZZLE_INPUT_FILE = "puzzle_input.txt"

if __name__ == "__main__":
    puzzle_input = open(PUZZLE_INPUT_FILE, "r").readlines()
    puzzle_input = [int(i) for i in puzzle_input]

    times = 0
    for i in range(1, len(puzzle_input)):
        if puzzle_input[i] > puzzle_input[i-1]:
            times += 1
    print(times)
